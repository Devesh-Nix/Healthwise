# 🧠 MCMI-III Psychological Test System (Django)

A web-based diagnostic tool built with Django that allows clinicians to register, manage patients, and conduct the MCMI-III psychological assessment with automated scoring and reporting.

---

## 🚀 Features

- 🔐 Clinician Signup/Login/Logout
- 🧑‍⚕️ Clinician Profile Management (with photo upload)
- 👥 Add & manage patients (per clinician)
- 🧪 Conduct the MCMI-III Test with all 175 questions
- 📊 Scoring, BR conversions, interpretations
- 🧾 Auto-generated Reports per patient per test attempt
- 📂 View previous test attempts
- 🖼 Beautiful, mobile-friendly Bootstrap UI

---

## 📁 Project Structure


- will be updated soon



---

## ⚙️ Setup Instructions

1. Clone the Repo
```bash
git clone https://github.com/yourusername/mcmi-test-system.git
cd mcmi-test-system
```

2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install Requirements
```bash
pip install -r requirements.txt
```

4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

6. Run Development Server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Environment Settings
In `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

In `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📄 License
MIT License. Free to use, customize, and build on.

