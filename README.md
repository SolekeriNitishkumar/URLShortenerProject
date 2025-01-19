# URLShortenerProject
--------------------------
Overview and Features
---------------------------
1. This is a Django-based URL shortener system that allows users to:
2. Shorten long URLs.
3. Set expiration times for shortened URLs.
4. Track analytics such as access count and logs.
5. Store data in an SQLite database.

Prerequisites
--------------
1. Python (3.8 or higher)
2. Django (4.0 or higher)
3. Django Rest Framework

Project Structure
------------------
URLShortenerProject
   -shortened_url/
          - manage.py
          - shortened_url/
                - __init__.py
                - asgi.py
                - settings.py
                - urls.py
                - wsgi.py
          - shortened_url_app/
                - __init__.py
                - admin.py
                - apps.py
                - models.py
                - serializers.py
                - urls.py
                - views.py
                - tests.py
                - migrations
          - db.sqlite3
   - Output Results.docx
   - Readme.md
   


Setup and Execution Instructions
---------------------------------
1. Clone the Repository from github using " git clone <repository_url>" or Download the Zip file. 
2. Navigate to "shortend_url" Directory in any code editor ( Preferred Visual Studio Code).
3. Install the Dependencies if Prerequisites are not installed using "pip install django djangorestframework" (Ignore if already installed).
4. Apply DB Migrations using below command in terminal
   - py manage.py makemigrations
   - python manage.py migrate
6. Create a Superuser to access Django admin panel (DB data can be viewed) using below command in terminal
   - python manage.py createsuperuser
   - Note: Follow the prompts to set up a username, email, and password.
7.  Start the Development Server using below command in terminal
   - python manage.py runserver

URL'S or API Endpoints Present
---------------------------
1. POST /shorten
2. GET  /<short_url>
3. GET /analytics/<short_url>


Request and Response Example for Each API Endpoint
----------------------------------------------
1. POST /shorten

Description: Create a shortened URL.

Request:

{
  "original_url": "https://example.com",
  "expires_in_hours": 48
}

Response:
{
  "original_url": "https://example.com",
  "short_url": "abc123",
  "expires_at": "2025-01-21T10:00:00Z"
}

2. GET /<short_url>   

Description: Redirect to the original URL if the link is not expired.

Request: Visit the short URL, e.g., http://127.0.0.1:8000/abc123/.

Response: Redirects to the original URL.  ( In Postman user will get HTML Response)

3. GET /analytics/<short_url>

Description: Retrieve analytics for a specific shortened URL.

Request: http://127.0.0.1:8000/analytics/abc123/

Response:
{
  "original_url": "https://example.com",
  "short_url": "abc123",
  "created_at": "2025-01-19T10:00:00Z",
  "expires_at": "2025-01-21T10:00:00Z",
  "access_count": 3,
  "access_logs": [
     {"timestamp": "2025-01-19T11:00:00Z", "ip_address": "127.0.0.1"}, 
     
     {"timestamp": "2025-01-19T12:30:00Z", "ip_address": "127.0.0.2"},
    {"timestamp": "2025-01-19T15:00:00Z", "ip_address": "127.0.0.3"}
  ]
}


Viewing Database Data
----------------------
1. Using Django Admin
    - Start the server using below command:
          - python manage.py runserver
     - Log in to the admin panel using superuser created early (step 6 of setup and execution instrutions) at http://127.0.0.1:8000/admin/
    - Navigate to:
        - Shortened URLs: View and manage shortened URLs.
        - Access Logs: View access logs.
   

   
    



