#!/bin/sh

pip install -r requirements.txt
if [[ -z "$1" ]]; then
    python import.py $1
fi
python manage.py syncdb
python manage.py runserver
