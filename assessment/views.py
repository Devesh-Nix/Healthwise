from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Response
from patients.models import Patient
from .scoring_keys import score_mcmi_iii
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required

from .models import TestSession
from django.utils import timezone
from .models import TestSession
from collections import defaultdict

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
from django.core.paginator import Paginator

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

grouped_results = defaultdict(list)

def generate_report_attempt(request, patient_id, attempt):
    # Get patient
    patient = get_object_or_404(Patient, id=patient_id)

    # Fetch responses using patient + attempt (as value)
    responses = Response.objects.filter(patient=patient, attempt=attempt)
    
    # Convert responses to dictionary format expected by scoring function
    response_dict = {r.question.number: r.answer for r in responses}

    # Run MCMI-III scoring on the responses
    result = score_mcmi_iii(response_dict, gender=patient.gender.lower())

    # Group results by section
    grouped_results = defaultdict(list)
    for scale, data in result['results'].items():
        section = data.get("section", "Other")
        grouped_results[section].append((scale, data))

    # Render the report
    return render(request, 'report.html', {
        'patient': patient,
        'attempt': attempt,
        'valid': result['valid'],
        'elevated_scales': result.get('elevated_scales', []),
        'clinical_concerns': result.get('clinical_concerns', []),
        'grouped_results': dict(grouped_results),
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

    # Fetch all questions and paginate them
    questions = Question.objects.all().order_by('number')
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bulk_upload.html', {'page_obj': page_obj})
