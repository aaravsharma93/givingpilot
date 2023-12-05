#!/bin/sh
python manage.py collectstatic --noinput
#python manage.py runserver 0.0.0.0:80
python manage.py migrate
gunicorn --workers=3 --bind 0.0.0.0:8000 'giving_pilot.wsgi:application'
