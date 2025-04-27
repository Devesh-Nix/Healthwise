# 🏥 HealthEase - Comprehensive Healthcare Management System

HealthEase is a web-based healthcare management platform built with Django. It provides a seamless experience for clinicians, patients, and administrators to manage appointments, medicines, services, and psychological assessments. The platform is designed to be user-friendly, mobile-responsive, and feature-rich.

---

## 🚀 Features

### 1. **User Roles**
- **Clinician/Doctor**: Manage patient profiles, conduct psychological tests, and view reports.
- **Patient/User**: Book appointments, order medicines, and access home services.
- **SuperAdmin**: Oversee the entire system, manage users, and monitor activities.

---

### 2. **Authentication**
- Secure login and signup for clinicians and patients.
- Password management with options to reset or change passwords.
- Role-based access control to ensure data privacy.

---

### 3. **Clinician Features**
- **Dashboard**: View and manage assigned patients.
- **Patient Management**:
  - Add new patients with details like name, DOB, gender, and email.
  - View patient history and medical records.
- **Psychological Testing**:
  - Conduct the MCMI-III test with 175 questions.
  - Automated scoring, BR conversions, and interpretations.
  - Generate detailed reports grouped by sections (e.g., Personality Patterns, Clinical Syndromes).
- **Profile Management**:
  - Update personal details like name, specialization, and clinic information.
  - Upload profile pictures.

---

### 4. **Patient Features**
- **Dashboard**: Access personalized features like booking appointments, ordering medicines, and availing home services.
- **Appointment Management**:
  - Book appointments with doctors by selecting date, time, and consultation mode (Chat, Video Call, Physical Visit).
  - View upcoming and past appointments.
- **Medicine Ordering**:
  - Browse available medicines with search functionality.
  - Add medicines to the cart and place orders.
  - View order history.
- **Home Services**:
  - Book local services like nurses, caretakers, cleaners, and chefs.
  - Specify service details like date, time, and duration.
- **Profile Management**:
  - Update personal details and view medical history.

---

### 5. **SuperAdmin Features**
- **Dashboard**:
  - View system statistics like total appointments, medicine orders, and service bookings.
  - Monitor recent activities across the platform.
- **Quick Actions**:
  - Add new doctors, medicines, and local services.
  - Manage user accounts and permissions.
- **Trends Overview**:
  - Visualize data trends using charts (e.g., appointments, medicines, services).

---

### 6. **Ambulance Services**
- Browse available ambulance providers with details like city, contact number, and base price.
- Book ambulance services by providing patient details, pickup address, and emergency type (Normal or Critical).

---

### 7. **Medicine Management**
- **For Admins**:
  - Add and manage medicines with details like name, description, price, and stock.
- **For Patients**:
  - Browse medicines with search and filter options.
  - Add medicines to the cart and proceed to checkout.
  - View cart summary with total cost.

---

### 8. **Home Services**
- Browse available service providers with details like name, service type, experience, hourly rate, and city.
- Book services by specifying client details, address, date, time, and duration.

---

### 9. **Psychological Assessment**
- Conduct MCMI-III tests for patients.
- Automated scoring and BR conversions.
- Generate detailed reports with interpretations and clinical concerns.
- View previous test attempts and their statuses.

---

### 10. **Admin Panel**
- Manage all models (e.g., Doctors, Patients, Medicines, Services, Appointments) via Django's admin interface.
- Perform CRUD operations on all entities.

---

### 11. **Responsive Design**
- Fully responsive UI built with Bootstrap 5.
- Optimized for both desktop and mobile devices.

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   git clone https://github.com/yourusername/healthease.git
   cd healthease

2. **Create & Activate Virtual Environment**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3.  Install Dependencies
    pip install -r requirements.txt

4. Run Migrations
    python manage.py makemigrations
    python manage.py migrate

5. Create Superuser
    python manage.py createsuperuser

6. Run Development Server
    python manage.py runserver

7. Access the Application
    Visit: http://127.0.0.1:8000

📄 License
This project is licensed under the MIT License. See the LICENSE file for details. ```