# Product Lead Management
A full-stack application built with Django (backend) and React (frontend) for managing products and leads,
with CRUD operations and report generation.

# Features Backend (Django)

1. Lead Management: Create leads through an open API (no authentication required).
• Reporting APIs:
2. Fetch leads created between two dates.
3. Retrieve top 10 products with the most leads.
4. Retrieve bottom 10 products with the least leads.
5. Determine how many products each lead has inquired about.

API Documentation: Swagger integration for easy API testing and exploration.



Clone the Repository:
git clone https://github.com/username/backend-repository.git



Navigate to the Project Directory:
cd myproject


Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate  


Install Dependencies:
pip install -r requirements.txt



Apply Migrations:
python manage.py makemigrations
python manage.py migrate

Run the Development Server:
python manage.py runserver


Integrate CORS Headers (for frontend communication):
pip install django-cors-headers


Access the Swagger API Documentation: After running the server, you can access the Swagger documentation at:
http://127.0.0.1:8000/swagger/

# Frontend (React)
User-friendly interface for managing products.
Login/Logout functionality for users.
Backend Installation Guide


Frontend Installation Guide
Navigate to the Frontend Directory:
cd frontend


Install Dependencies:
npm install


Run the Development Server:
npm start


# Frontend Screenshots
# UI Overview

<img width="917" alt="Screenshot 2024-09-05 142118" src="https://github.com/user-attachments/assets/c955941b-5c98-4404-a47b-7d35ca98ebb0">

 <img width="915" alt="Screenshot 2024-09-05 142221" src="https://github.com/user-attachments/assets/2f2e3c0d-6540-4596-bf7a-033972ea8b3d">

 <img width="916" alt="Screenshot 2024-09-05 142324" src="https://github.com/user-attachments/assets/0745214e-7773-4b52-96fa-7559dac31af1">

 <img width="921" alt="Screenshot 2024-09-05 142428" src="https://github.com/user-attachments/assets/5e57ef9a-329d-4c1e-983f-68d108ea8b8e">
