# Blog Engine in Django Restframework 
### (Work in Progress)


<p>
A blog engine backend constructed in django restframework with custom user models and login.
</p>

## Setup:

1. Create a ```virtualenv``` named such as ```env``` and switch to it.
2. Run: ```python -m pip install --upgrade pip``` to upgrade the ```PythonPackageManager``` (just to save you an hour's worth of headache 5 minutes later).
3. Run: ```pip install -r requirements.txt```
4. Run: [```chmod +x run.sh``` , ```chmod +x migrate.sh```]
5. Create the ```.env``` file and fill the values as per the format given below.
6. Run: ```./migrate.sh```
7. Run: ```python manage.py createsuperuser```

    7.1. Enter the superuser credentials as required.
8. Run: ```./run.sh```

## Basic Level 0 control flow:

1. Create a ```user```.
2. Generate an ```author``` from a ```user```.
3. Whenever a new ```blog post``` is added, the ```author``` is derived from ```request.user``` and added to the ```blog post```.
4. A ```blog post``` can only be updated or deleted if ```request.user``` is either the owning user or a member of the staff.
5. The list of all users can only be viewed/deleted if ```request.user``` is an administrator or a member of the staff.

## Installed Custom Applications:

1. Userapp:

    Used for user registration and verification via author-generation.

2. Blogapp:

    Used to CRUD blog posts in/from the database.

### .env File Format:

```
SECRET_KEY = ''
DATABASE = ''
USER = ''
PASSWORD = ''
HOST = ''
PORT = 
DEBUG = 
```

### Documentation:

[documenter.getpostman.com](https://documenter.getpostman.com/view/17779018/UVXnFtk8)