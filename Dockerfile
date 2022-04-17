FROM python:slim-buster
# FROM postgres:12.2

# RUN sudo -u postgres psql -c "CREATE USER prithoo WITH PASSWORD 'password';"
# RUN sudo -u postgres psql -c "CREATE DATABASE blogdjango;"
# RUN sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE blogdjango TO prithoo;"

WORKDIR /blogappDRF

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

## ENV Database Settings:
ENV DATABASE = 'blogdjango'
ENV USER = 'prithoo'
ENV PASSWORD = 'password'
ENV HOST = 'localhost'
ENV PORT = 5432

## ENV Site Settings:
ENV DEBUG = True
ENV LANGUAGE_CODE = 'en-us'
ENV TIME_ZONE = 'Asia/Kolkata'
ENV USE_I18N = True
ENV USE_TZ = True

## ENV AWS S3 Settings:
ENV AUDIO_POST_URL = 'https://s3.amazonaws.com/audiopostapp-audio-files/'

COPY . .

# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py createsuperuser


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]