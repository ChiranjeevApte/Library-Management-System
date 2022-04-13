# Library-Management-System

To Run this project, 

1. create database naming library in mysql.

2. Go to [library_management_system -> settings.py](library_management_system/settings.py)   and Enter your user and password in DATABASES part.

3. then run following commands:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   python3 manage.py runserver
   ```
4. After Server is up and running [Click here](http://127.0.0.1:8000/).

5. Login page will appear. Login with Email-id and Password set while creating super user.

6. After Login, we can see the tables Books.

7. Change URL to [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/) to Create, Update, delete or view the books.

Thank You !!!
