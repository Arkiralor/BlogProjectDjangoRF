# Blog Engine in Django Restframework 

_A blog-engine Rest API constructed in django restframework with custom user models and login._

## Definition

<p> A blog-engine is a a software or tool which let’s one create and manage a blog or website. </p>

<p> Conventional websites are a collection of web pages that are accessible from a website. A blog differs from a website in that it is generally managed using a blogging platform which stores your content, media, files, links and all other necessary things required for the operation and working of your blogs which are created by the users of the site and not the administrators. </p>

_Social Media Websites can be considered the technological descendants of the original blog-engine concept, popularized in the early 2000s._

__Source__: [cultofweb.com](https://cultofweb.com/blog/blogging-platforms-compared/)

## Basic Level 0 Control Flow

1. Sign up a new ```user``` if not already registered.
2. Generate an ```author``` from the new ```user``` if not already generated.
3. Whenever a new ```blog post``` is added, the ```author``` is derived from ```request.user``` and added to the ```blog post``` model object.
4. A ```blog post``` can only be updated or deleted if ```request.user``` is either the owning user or a member of the staff.
5. The list of all users can only be viewed/deleted if ```request.user``` is a member of the staff.

### Details

1. __Type__: REST API
2. __Authentication__: Token Authetication
3. __Database Type__: Relational
4. __Database__: PostgreSQL
5. __Types of Users__: Superuser, Staff, User
6. __Timezone__: Asia/Kolkata (UTC +05:30hrs)

## Development Environment Setup

1. Create a ```virtualenv``` named such as ```env``` and switch to it.
2. Run: ```python -m pip install --upgrade pip``` to upgrade the ```PythonPackageManager``` (just to save you an hour's worth of headache 5 minutes later).
3. Run: ```pip install -r requirements.txt```
4. Run: [
    ```chmod +x run.sh``` ,
    ```chmod +x migrate.sh```,
    ```chmod +x shell.sh```
    ]
5. Create the ```.env``` file and fill the values as per the format given below.
6. Run: ```./migrate.sh```
7. Run: ```python manage.py createsuperuser```

    7.1. Enter the superuser credentials as required.
8. Run: ```./run.sh``` to run the server.

    8.1. Run: ```./shell.sh``` to run the shell when required.

## Installed Custom Applications

1. [Userapp](https://github.com/Arkiralor/BlogProjectDjangoRF/tree/master/userapp):

    Used for user registration and verification via author-generation.

2. [Blogapp](https://github.com/Arkiralor/BlogProjectDjangoRF/tree/master/blogapp):

    Used to perform CRUD operations on blog posts in/from the database.

### .env File Format

``` ENV
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
_(To be updated...)_

### Collaboraters & (C)

1. [Prithoo Medhi](https://github.com/Arkiralor), 2021
