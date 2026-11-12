
# Internship Portal – Django Backend

A RESTful backend application built using Django and Django REST Framework to manage internship programs and student applications.

This project demonstrates backend development concepts including REST APIs, JWT authentication, role-based permissions, PostgreSQL database integration, input validation, and automated testing.


## Technologies Used

- **Language:** Python
- **Backend Framework:** Django
- **API Framework:** Django REST Framework
- **Authentication:** JWT (Simple JWT)
- **Database:** PostgreSQL
- **API Documentation:** Swagger / OpenAPI
- **API Testing:** Postman
- **Automated Testing:** Django TestCase, pytest, pytest-django
- **Version Control:** Git and GitHub


## Features

- Create, retrieve, update, and delete internship programs.
- Manage student internship applications.
- JWT-based authentication using access and refresh tokens.
- Role-based access control for students and staff.
- Application ownership permissions.
- Filter, search, sort, and paginate internship programs.
- Input validation and structured error handling.
- PostgreSQL database integration.
- API documentation using Swagger / OpenAPI.
- Application logging and security configurations.
- Automated tests for models, API endpoints, permissions, and validation.


## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/DasaradhChitturu/internship-portal-django.git
cd internship-portal-django
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg python-dotenv drf-spectacular pytest pytest-django
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and update the values with your local database credentials and Django secret key.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

http://127.0.0.1:8000/


## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtain JWT access and refresh tokens |
| POST | `/api/token/refresh/` | Generate a new access token |

### Internship Programs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/programs-viewset/` | List internship programs |
| POST | `/api/programs-viewset/` | Create an internship program |
| GET | `/api/programs-viewset/{id}/` | Retrieve a program |
| PATCH | `/api/programs-viewset/{id}/` | Partially update a program |
| PUT | `/api/programs-viewset/{id}/` | Update a program |
| DELETE | `/api/programs-viewset/{id}/` | Delete a program |

### Student Applications

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/applications/` | List accessible applications |
| POST | `/api/applications/` | Submit an application |
| GET | `/api/applications/{id}/` | Retrieve an application |
| PATCH | `/api/applications/{id}/` | Partially update an application |
| PUT | `/api/applications/{id}/` | Update an application |
| DELETE | `/api/applications/{id}/` | Delete an application |


## Running Tests

Run all automated tests using pytest:

```bash
python -m pytest -v
```

Run Django application tests:

```bash
python manage.py test core
```

The test suite covers:

- Model creation and validation.
- API response status codes.
- Authentication and authorization.
- Student and staff permissions.
- Invalid input handling.
- Missing resource handling.
- Salary calculation logic.


## Project Status

This project was developed as part of a hands-on Python Backend Development learning roadmap. It demonstrates practical implementation of Django REST APIs, authentication, database integration, permissions, and automated testing.

## Author

**Dasaradha Ram Chitturu**

GitHub: [DasaradhChitturu](https://github.com/DasaradhChitturu)


## API Development Workflow

New API features are developed in separate Git feature branches.

Before merging into the main branch:

- Implement the API functionality.
- Write automated tests.
- Verify API responses.
- Submit a Pull Request for code review.