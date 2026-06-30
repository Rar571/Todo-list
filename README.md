# TODO List Web Application

A clean, minimalist web application for managing daily tasks and tracking deadlines, built with the **Django** framework.

## 🚀 Features

- **Task Management:** Full CRUD (Create, Read, Update, Delete) functionality for handling tasks.
- **Quick Status Toggle:** Easily mark tasks as *Complete* or *Undo* with a single click.
- **Tagging System:** Organize tasks into custom categories (e.g., *work*, *home*, *shop*) with full tag management.
- **Deadline Tracking:** Keep an eye on your task schedules with a built-in deadline feature.
- **Minimalist Interface:** A lightweight, distraction-free UI leveraging basic Bootstrap layout components.

---

## 🛠️ Tech Stack

- **Backend:** Python / Django
- **Database:** SQLite 
- **Frontend:** HTML, CSS, Bootstrap 5

---

## 📦 Local Setup Instructions

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Rar571/Todo-list.git
cd https://github.com/Rar571/Todo-list.git
```
### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Database Migrations
```bash
python manage.py migrate
```
### 5. Create a Superuser (For Django Admin access)
```bash
python manage.py createsuperuser
```
### 6. Start the development server
```bash
python manage.py runserver
```
Open your browser and navigate to: http://127.0.0.1:8000/
## 📂 Project Structure
### A quick overview of the main application layout:
- todo/ — Core application directory containing logic (Views, Models, Forms, URLs).
- todo/templates/ — HTML interface layout (base.html, lists, and form screens).
- todo_project/ — Root project configuration folder (settings.py, urls.py).
