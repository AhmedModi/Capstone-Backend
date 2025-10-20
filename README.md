# Capstone Backend Project - E-commerce API

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://djangoproject.com)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.16-red.svg)](https://www.django-rest-framework.org)
[![JWT](https://img.shields.io/badge/JWT-Authentication-orange.svg)](https://jwt.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive REST API for an e-commerce platform built with Django and Django REST Framework. This project demonstrates full-stack development skills with authentication, product management, and comprehensive API documentation.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation & Setup](#installation--setup)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

This backend API serves as the foundation for an e-commerce platform, providing endpoints for user management, product catalog, authentication, and more. Built following Django best practices with comprehensive documentation and testing.

### ALX Capstone Project Criteria Met:

✅ **Backend Development**: Full Django REST API implementation  
✅ **Authentication & Authorization**: JWT-based authentication system  
✅ **Database Design**: Well-structured models with relationships  
✅ **API Documentation**: Comprehensive Swagger/OpenAPI documentation  
✅ **Testing**: Unit tests and API endpoint testing  
✅ **Deployment**: Production-ready configuration  
✅ **Code Quality**: Clean, documented, and maintainable code  
✅ **Version Control**: Git with proper commit history  

## 🚀 Features

### Core Features
- **User Management**: Registration, authentication, and profile management
- **Product Catalog**: CRUD operations for products with categories
- **Authentication**: JWT-based authentication with refresh tokens
- **Search & Filtering**: Advanced search and filtering capabilities
- **Pagination**: Efficient data pagination for large datasets
- **API Documentation**: Interactive Swagger UI documentation

### Technical Features
- **RESTful API Design**: Following REST principles
- **Database Relationships**: Proper foreign key relationships
- **Input Validation**: Comprehensive data validation
- **Error Handling**: Proper HTTP status codes and error responses
- **Security**: CSRF protection, input sanitization, and secure headers
- **Performance**: Optimized queries with select_related and prefetch_related

## 🛠 Technology Stack

### Backend
- **Python 3.11+** - Programming language
- **Django 5.2** - Web framework
- **Django REST Framework 3.16** - API framework
- **Django Simple JWT** - JWT authentication
- **Django Filter** - Advanced filtering
- **drf-yasg** - Swagger documentation

### Database
- **SQLite** - Development database
- **PostgreSQL** - Production database (ready for deployment)

### Development Tools
- **Git** - Version control
- **Virtual Environment** - Dependency isolation
- **Pip** - Package management

## 📦 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Git
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/AhmedModi/Capstone-Backend.git
cd Capstone-Backend
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📚 API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **JSON Schema**: http://localhost:8000/swagger.json

### API Endpoints

#### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

#### Products
- `GET /api/products/` - List all products
- `POST /api/products/` - Create new product
- `GET /api/products/{id}/` - Get specific product
- `PUT /api/products/{id}/` - Update product
- `PATCH /api/products/{id}/` - Partially update product
- `DELETE /api/products/{id}/` - Delete product

#### Users
- `GET /api/users/` - List users (admin only)
- `POST /api/users/` - Create new user
- `GET /api/users/{id}/` - Get user profile
- `PUT /api/users/{id}/` - Update user profile

### Query Parameters

#### Products Endpoint
- `search` - Search in name and description
- `min_price` - Filter by minimum price
- `max_price` - Filter by maximum price
- `category` - Filter by category name
- `ordering` - Sort by field (price, name, created_at)
- `page` - Page number for pagination

#### Example Requests
```bash
# Search products
GET /api/products/?search=laptop

# Filter by price range
GET /api/products/?min_price=100&max_price=1000

# Sort by price
GET /api/products/?ordering=price

# Combine filters
GET /api/products/?search=phone&min_price=200&ordering=-created_at
```

## 🔐 Authentication

### JWT Authentication Flow

1. **Obtain Token**:
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

2. **Use Token in Requests**:
```bash
curl -H "Authorization: Bearer your_jwt_token" \
  http://localhost:8000/api/products/
```

3. **Refresh Token**:
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

### Token Configuration
- **Access Token Lifetime**: 5 minutes
- **Refresh Token Lifetime**: 1 day
- **Algorithm**: HS256

## 🗄 Database Schema

### Models

#### User Model
```python
- id: Primary key
- username: Unique username
- email: Email address
- first_name: First name
- last_name: Last name
- is_active: Account status
- date_joined: Registration date
```

#### Product Model
```python
- id: Primary key
- name: Product name
- slug: URL-friendly name
- description: Product description
- price: Product price (DecimalField)
- stock: Available quantity
- category: Foreign key to Category
- image_url: Product image URL
- owner: Foreign key to User
- created_at: Creation timestamp
- updated_at: Last update timestamp
```

#### Category Model
```python
- id: Primary key
- name: Category name (unique)
```

### Relationships
- Product → Category (Many-to-One)
- Product → User (Many-to-One, for product ownership)
- User → Product (One-to-Many, through reverse relationship)

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test products
python manage.py test users

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Coverage
The project includes tests for:
- Model validation and methods
- API endpoint functionality
- Authentication flows
- Permission checks
- Serializer validation
- Filter and search functionality

### Manual Testing with curl

#### Create a Product
```bash
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product",
    "description": "A test product description",
    "price": 29.99,
    "stock": 10,
    "image_url": "https://example.com/image.jpg"
  }'
```

#### Search Products
```bash
curl "http://localhost:8000/api/products/?search=test"
```

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL database
4. Set up static file serving
5. Configure environment variables

### Environment Variables
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Deployment Platforms
- **PythonAnywhere** (recommended for beginners)
- **Heroku**
- **DigitalOcean**
- **AWS EC2**

## 📁 Project Structure

```
Capstone-Backend/
├── config/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── products/              # Products app
│   ├── models.py         # Product and Category models
│   ├── views.py          # API views
│   ├── serializers.py    # Data serializers
│   ├── urls.py          # App URL patterns
│   ├── admin.py         # Admin interface
│   └── migrations/      # Database migrations
├── users/                # Users app
│   ├── models.py        # User model
│   ├── views.py         # User views
│   ├── serializers.py   # User serializers
│   ├── urls.py         # User URL patterns
│   ├── admin.py        # Admin interface
│   └── migrations/     # Database migrations
├── venv/                # Virtual environment
├── db.sqlite3          # SQLite database
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write tests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dahiru Ahmed**
- GitHub: [@AhmedModi](https://github.com/AhmedModi)
- Project: ALX Capstone - Backend Development

## 🙏 Acknowledgments

- ALX Software Engineering Program
- Django and Django REST Framework communities
- Open source contributors

---

## 📞 Support

If you have any questions or need help with this project, please:

1. Check the [Issues](https://github.com/AhmedModi/Capstone-Backend/issues) page
2. Create a new issue if your question hasn't been answered
3. Contact the author directly

**Happy Coding! 🚀**
