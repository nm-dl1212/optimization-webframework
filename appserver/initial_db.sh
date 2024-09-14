#!/bin/bash
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com
export DJANGO_SUPERUSER_PASSWORD=admin123
python manage.py createsuperuser --noinput

python manage.py makemigrations
python manage.py migrate