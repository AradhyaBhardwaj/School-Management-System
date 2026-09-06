Student Management System

A web-based academic management platform built with Python and Django. The application brings common college administration tasks into one place and gives each user a focused dashboard based on their role.

## Overview

The system supports three user roles: **HOD/Admin**, **Staff**, and **Student**. Administrators can manage the academic structure and review requests, staff members can handle attendance and results, and students can access their academic information and communicate with the administration.

## Features

### HOD/Admin

- View academic activity through dashboard summaries
- Add, update, and remove staff members and students
- Manage courses, subjects, and academic sessions
- Review student and staff attendance
- Approve or reject leave applications
- Read and reply to feedback

### Staff

- View a staff dashboard with relevant academic information
- Take and update student attendance
- Add and update student results
- Apply for leave
- Send feedback to the HOD

### Students

- View personal attendance and results
- Submit leave applications
- Send feedback to the administration
- Update profile information

## Technology Stack

- Python
- Django
- SQLite
- HTML, CSS, and JavaScript
- Bootstrap
- Chart.js

## Getting Started

### Requirements

- Python 3.10 or later
- pip
- Git

### Installation

1. Clone the repository and open its directory:

   ```bash
   git clone <your-repository-url>
   cd student-management-system
   ```

2. Create and activate a virtual environment.

   **Windows:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create an administrator account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000/` in a browser to use the application.

## Project Structure

- `student_management_app/` contains the models, views, forms, authentication, and application URLs.
- `student_management_system/` contains the Django project configuration.
- `templates/` and `static/` contain the user interface resources.
- `db.sqlite3` is the local development database.

## Developer

**Aradhya Bhardwaj**
