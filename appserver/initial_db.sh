#!/bin/bash

# migration
python manage.py makemigrations api
python manage.py migrate

# superuser
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=admin123
python manage.py createsuperuser --noinput
