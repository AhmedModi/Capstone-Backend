```markdown
# Capstone Backend Project

This repository contains the backend for the Capstone project, built with **Django** and **Django REST Framework (DRF)**.  
The project is structured into modular apps to ensure scalability and clean separation of concerns.

---

## 📌 Project Structure

```

Capstone-Backend/
│── config/              # Django project settings
│── users/               # Users app (authentication, profiles)
│── products/            # Products app (management, listings)
│── requirements.txt     # Project dependencies
│── manage.py            # Django management script
│── README.md            # Project documentation

````

---

## ✅ What I Have Accomplished So Far

- Initialized a Django project (`config`) with REST framework support.  
- Created two main apps: `users` and `products`.  
- Set up a GitHub repository for version control.  
- Designed an initial ERD (Entity Relationship Diagram).  
- Prepared environment setup instructions for local development.  
- Drafted `.gitignore` and `requirements.txt`.  

---

## ⚡ Challenges Faced & How They Were Handled

- **Structuring the ERD clearly so that it aligns with project goals**  
  🔹 *Solution:* Iterated the ERD design step by step and simplified relationships into `User` and `Product` base entities first.  

- **Planning Django app modularity (separating users and products)**  
  🔹 *Solution:* Created dedicated apps for `users` and `products` to ensure clean separation of concerns.  

- **Understanding deployment options (local vs. PythonAnywhere)**  
  🔹 *Solution:* Chose **PythonAnywhere** for deployment and will start with basic Django auth before scaling.  

- **Environment setup & migrations issue on Python 3.13**  
  🔹 *Solution:* Rebuilt the virtual environment, reinstalled Django/DRF, and verified missing files. Considering fallback to **Python 3.11 (LTS)** for stability.  

---

## 🚀 What’s Next? (Upcoming Week Plan)

- Finalize initial models for `User` and `Product`.  
- Run migrations successfully after fixing the environment mismatch.  
- Implement basic Django authentication.  
- Deploy the project on **PythonAnywhere**.  
- Document setup instructions clearly in the `README.md`.  

---

## 🔧 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/Capstone-Backend.git
cd Capstone-Backend
````

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

---

## 📚 Tech Stack

* **Python 3.11+** (recommended for stability)
* **Django 5.1**
* **Django REST Framework (DRF)**
* **SQLite (development)** → will scale to **PostgreSQL** for production
* **PythonAnywhere** for deployment

---

✍️ **Author:** Dahiru Ahmed
📌 Capstone Project – Backend Development Journey


