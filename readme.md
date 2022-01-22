# Blog Engine in Django Restframework 

<p>
A blog-engine Rest API constructed in django restframework with custom user models and login.
</p>

### Definition:

<p>
A blogg-engine is a a software or tool which let’s one create and manage a blog or website.

Conventional websites are a collection of web pages that are accessible from a website. A blog differs from a website in that it is generally managed using a blogging platform which stores your content, media, files, links and all other necessary things required for the operation and working of your blogs which are created by the users of the site and not the administrators.

Social Media Websites can be considered the technological descendants of the original blog-engine concept, popularized in the early 2000s.
</p>

__Source__: [cultofweb.com](https://cultofweb.com/blog/blogging-platforms-compared/)

### Details:

1. __Type__: REST API
2. __Authentication__: Token Authetication
3. __Types of Users__: Superuser, Staff, User
4. __Timezone__: Asia/Kolkata (UTC +05:30hrs)

## Development Environment Setup:

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

1. [Userapp](https://github.com/Arkiralor/BlogProjectDjangoRF/tree/master/userapp):

    Used for user registration and verification via author-generation.

2. [Blogapp](https://github.com/Arkiralor/BlogProjectDjangoRF/tree/master/blogapp):

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