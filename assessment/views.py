from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Response
from patients.models import Patient
from .scoring_keys import SCORING_KEYS
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required

from .models import TestSession
from django.utils import timezone
from .models import TestSession

import csv
import mimetypes
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question
from io import TextIOWrapper
import openpyxl
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, TestSession, Response, Question

@login_required
def add_patient(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST.get('email', '')

        Patient.objects.create(
            clinician=request.user,
            full_name=full_name,
            dob=dob,
            gender=gender,
            email=email
        )
        messages.success(request, "Patient added successfully.")
        return redirect('add_patient')

    return render(request, 'add_patient_select_test.html')

@login_required
def select_test(request):
    patients = Patient.objects.filter(clinician=request.user)

    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        test_name = request.POST['test_name']

        if test_name == "MCMI-III":
            return redirect('take_test', patient_id=patient_id)

        messages.warning(request, "This test is not available yet.")
        return redirect('select_test')

    return render(request, 'add_patient_select_test.html', {"patients": patients})

# def generate_report(request, patient_id):
#     patient = get_object_or_404(Patient, id=patient_id)
#     responses = Response.objects.filter(patient=patient)

#     report_data = []

#     for scale, data in SCORING_KEYS.items():
#         score = 0
#         for qn in data['questions']:
#             try:
#                 question = Question.objects.get(number=qn)
#                 response = responses.get(question=question)
#                 if response.answer:
#                     score += 1
#             except (Question.DoesNotExist, Response.DoesNotExist):
#                 continue

#         interpretation = data['interpretation'](score)
#         br_score = data['br_conversion'](score)
#         report_data.append({
#             'scale': scale,
#             'raw_score': score,
#             'br_score': br_score,
#             'interpretation': interpretation
#         })

#     return render(request, 'assessment/report.html', {
#         'patient': patient,
#         'report_data': report_data
#     })

@staff_member_required
def admin_dashboard(request):
    session_count = TestSession.objects.count()
    completed_sessions = TestSession.objects.filter(completed_at__isnull=False).count()
    patients_tested = Patient.objects.annotate(attempts=Count('testsession')).filter(attempts__gt=0).count()

    sessions = TestSession.objects.select_related('patient').order_by('-started_at')[:10]  # latest 10

    return render(request, 'admin_dashboard.html', {
        'session_count': session_count,
        'completed_sessions': completed_sessions,
        'patients_tested': patients_tested,
        'latest_sessions': sessions
    })


def patient_attempts(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    sessions = TestSession.objects.filter(patient=patient).order_by('-attempt_number')

    return render(request, 'patient_attempts.html', {
        'patient': patient,
        'sessions': sessions
    })



def take_test(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    # Get latest attempt number
    last_session = TestSession.objects.filter(patient=patient).order_by('-attempt_number').first()
    attempt = last_session.attempt_number + 1 if last_session else 1

    session, created = TestSession.objects.get_or_create(patient=patient, attempt_number=attempt)

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('question_'):
                qid = int(key.split('_')[1])
                answer = True if value == 'true' else False
                question = Question.objects.get(id=qid)

                Response.objects.update_or_create(
                    patient=patient,
                    question=question,
                    attempt=attempt,
                    defaults={'answer': answer}
                )
        session.completed_at = timezone.now()
        session.save()
        return redirect('generate_report_attempt', patient_id=patient.id, attempt=attempt)

    questions = Question.objects.all().order_by('number')
    return render(request, 'take_test.html', {
        'patient': patient,
        'questions': questions,
        'attempt': attempt
    })

def generate_report_attempt(request, patient_id, attempt):
    patient = get_object_or_404(Patient, id=patient_id)
    responses = Response.objects.filter(patient=patient, attempt=attempt)

    report_data = []

    for scale, data in SCORING_KEYS.items():
        score = 0
        for qn in data['questions']:
            try:
                question = Question.objects.get(number=qn)
                response = responses.get(question=question)
                if response.answer:
                    score += 1
            except:
                continue

        report_data.append({
            'scale': scale,
            'raw_score': score,
            'br_score': data['br_conversion'](score),
            'interpretation': data['interpretation'](score)
        })

    return render(request, 'report.html', {
        'patient': patient,
        'report_data': report_data,
        'attempt': attempt
    })


def bulk_upload_questions(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        if not file:
            messages.error(request, "No file selected.")
            return redirect('bulk_upload_questions')

        ext = file.name.split('.')[-1].lower()
        count = 0

        try:
            if ext == 'csv':
                decoded_file = TextIOWrapper(file, encoding='utf-8')
                reader = csv.DictReader(decoded_file)

                for row in reader:
                    number = int(row['number'])
                    text = row['text']
                    if not text:
                        continue
                    Question.objects.update_or_create(number=number, defaults={'text': text})
                    count += 1

            elif ext in ['xlsx', 'xls']:
                wb = openpyxl.load_workbook(file)
                sheet = wb.active
                for row in sheet.iter_rows(min_row=2, values_only=True):
                    if row and row[0] and row[1]:
                        number = int(row[0])
                        text = row[1]
                        Question.objects.update_or_create(number=number, defaults={'text': text})
                        count += 1

            else:
                messages.error(request, "Unsupported file format. Upload .csv or .xlsx only.")
                return redirect('bulk_upload_questions')

            messages.success(request, f"{count} questions uploaded successfully.")

        except Exception as e:
            messages.error(request, f"Error uploading file: {e}")

        return redirect('bulk_upload_questions')

    questions = Question.objects.all().order_by('number')
    return render(request, 'bulk_upload.html', {'questions': questions})
