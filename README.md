# Capstone Backend Project - E-commerce API

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://djangoproject.com)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.16-red.svg)](https://www.django-rest-framework.org)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange.svg)](https://jwt.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A robust REST API backend for an e-commerce platform built using Django and Django REST Framework (DRF). This project demonstrates backend development skills, including authentication, product management, filtering, search, and comprehensive API documentation.

---

## 📋 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technology Stack](#technology-stack)
* [Installation & Setup](#installation--setup)
* [API Documentation](#api-documentation)
* [Authentication](#authentication)
* [Database Schema](#database-schema)
* [Testing](#testing)
* [Deployment](#deployment)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
* [Author & Acknowledgments](#author--acknowledgments)
* [Support](#support)

---

## 🎯 Project Overview

This backend API is the foundation for an e-commerce platform. It provides endpoints for user management, product catalog, authentication, and administrative functions.

### ALX Capstone Project Compliance

✅ Backend development with Django REST Framework
✅ JWT Authentication & Authorization
✅ Fully designed database schema
✅ Swagger/OpenAPI API documentation
✅ Unit testing & API endpoint tests
✅ Production-ready deployment configuration
✅ Clean, modular, and maintainable code
✅ Version control with Git

---

## 🚀 Features

### Core Features

* **User Management**: Registration, login, profile management
* **Product Catalog**: CRUD operations for products and categories
* **Authentication**: JWT-based with access & refresh tokens
* **Search & Filtering**: Full-text search, filter by price/category, pagination
* **API Documentation**: Swagger UI and ReDoc integration

### Technical Features

* **RESTful API Design**: Following industry-standard practices
* **Database Relationships**: Proper foreign key relationships
* **Input Validation & Error Handling**: Robust and informative
* **Security**: JWT authentication, CSRF protection, secure headers
* **Performance**: Optimized queries using `select_related` & `prefetch_related`

---

## 🛠 Technology Stack

### Backend

* Python 3.11+
* Django 5.2
* Django REST Framework 3.16
* Django Simple JWT
* Django Filter (Advanced filtering)
* drf-yasg (Swagger/OpenAPI docs)

### Database

* SQLite (Development)
* PostgreSQL (Production-ready)

### Tools

* Git (Version control)
* Virtual Environment (Dependency isolation)
* pip (Package management)

---

## 📦 Installation & Setup

### Prerequisites

* Python 3.11+
* Git
* pip

### 1. Clone the repository

```bash
git clone https://github.com/AhmedModi/Capstone-Backend.git
cd Capstone-Backend
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Database setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

API will be available at `http://localhost:8000/`

---

## 📚 API Documentation

Interactive documentation available at:

* **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* **ReDoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

### Authentication Endpoints

* `POST /api/token/` → Obtain JWT token
* `POST /api/token/refresh/` → Refresh JWT token

### Product Endpoints

* `GET /api/products/` → List all products
* `POST /api/products/` → Create a product
* `GET /api/products/{id}/` → Retrieve a product
* `PUT /api/products/{id}/` → Update a product
* `PATCH /api/products/{id}/` → Partial update
* `DELETE /api/products/{id}/` → Delete a product

### User Endpoints

* `GET /api/users/` → List users (admin only)
* `POST /api/users/` → Create new user
* `GET /api/users/{id}/` → Get user profile
* `PUT /api/users/{id}/` → Update user profile

### Query Parameters for Products

* `search` → Search in name & description
* `min_price` / `max_price` → Filter by price range
* `category` → Filter by category name
* `ordering` → Sort results (e.g., `price`, `-created_at`)
* `page` → Pagination

---

## 🔐 Authentication

JWT authentication flow:

1. Obtain token:

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'
```

2. Use token in requests:

```bash
curl -H "Authorization: Bearer your_jwt_token" http://localhost:8000/api/products/
```

3. Refresh token:

```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"your_refresh_token"}'
```

---

## 🗄 Database Schema

### Models

**User**

* id, username, email, first_name, last_name, is_active, date_joined

**Product**

* id, name, slug, description, price, stock, category (FK), image_url, owner (FK), created_at, updated_at

**Category**

* id, name (unique)

**Relationships**

* Product → Category (Many-to-One)
* Product → User (Many-to-One)

---

## 🧪 Testing

Run all tests:

```bash
python manage.py test
```

Run specific app tests:

```bash
python manage.py test products
python manage.py test users
```

With coverage:

```bash
coverage run --source='.' manage.py test
coverage report
```

Tests cover:

* Models
* API endpoints
* Authentication & permissions
* Serializer validation
* Filtering, search, and pagination

---

## 🚀 Deployment

### Production Checklist

* Set `DEBUG=False`
* Configure `ALLOWED_HOSTS`
* Use PostgreSQL database
* Serve static files
* Set environment variables

---

## 📁 Project Structure

```
Capstone-Backend/
├── config/                 # Django settings
├── products/               # Products app
├── users/                  # Users app
├── venv/                   # Virtual environment
├── db.sqlite3              # SQLite DB
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/awesome-feature`
3. Commit changes: `git commit -m "Add awesome feature"`
4. Push branch: `git push origin feature/awesome-feature`
5. Open a Pull Request

---

## 👨‍💻 Author & Acknowledgments

**Author:** Dahiru Ahmed

* GitHub: [@AhmedModi](https://github.com/AhmedModi)

**Acknowledgments:**

* ALX Software Engineering Program
* Django & Django REST Framework communities
* Open source contributors

---

## 📞 Support

* Open an [Issue](https://github.com/AhmedModi/Capstone-Backend/issues)
* Contact the author directly

---

✅ **Ready for production and further enhancements**


