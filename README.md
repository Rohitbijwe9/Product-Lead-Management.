# 📚 Library Management System

An advanced backend solution built with Django and Django REST Framework to streamline library operations. This system empowers librarians to efficiently manage users, books, borrow requests, and track borrowing history, while allowing library users to browse books, make borrow requests, and view their borrowing history.

## 🌟 Features

### Librarian Functionality
- **User Management**: Create, update, and delete library users.
- **Book Management**: Add, update, and remove books in the library.
- **Request Management**: Approve or deny book borrow requests.
- **Borrow History**: View detailed borrowing history for all users.

### Library User Functionality
- **Book Catalog**: Browse and search for available books.
- **Borrow Requests**: Submit requests to borrow books for specific periods.
- **Borrow History**: View personal borrowing history in real-time.

## 🚀 Getting Started

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rohitbijwe9/Library-Management-System-.git
   cd Library-Management-System-

2. **Set Up Virtual Environment**:
    ```bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


3.**Install Dependencies**:
pip install -r requirements.txt


4.**Apply Migrations**:
python manage.py makemigrations
python manage.py migrate


5.**Create Superuser**:
python manage.py createsuperuser


6.**Run the Server**:
python manage.py runserver


7.**Access the Swagger API Documentation: After running the server, access the Swagger documentation at**:
http://127.0.0.1:8000/swagger/

8.**📝 API Endpoints**

Librarian Endpoints
http://127.0.0.1:8000/POST /api/users/: Create a new library user.
http://127.0.0.1:8000/PUT /api/users/{id}/: Update an existing library user.
http://127.0.0.1:8000/DELETE /api/users/{id}/: Delete a library user.
http://127.0.0.1:8000/GET /api/borrow-requests/: Get all borrow requests.
http://127.0.0.1:8000/PATCH /api/borrow-requests/{id}/: Approve or deny a borrow request.
http://127.0.0.1:8000/GET /api/history/: Get a list of borrow history.
Library User Endpoints
http://127.0.0.1:8000/GET /api/books/: Get a list of available books.
http://127.0.0.1:8000/POST /api/borrow-requests/: Submit a request to borrow a book.
http://127.0.0.1:8000/GET /api/history/{user_id}/: View personal borrow history.

9.**📑 API Documentation (Swagger)**
Swagger UI provides an interactive API documentation that makes it easy to test the endpoints.

Access the API documentation at:
http://127.0.0.1:8000/swagger/

