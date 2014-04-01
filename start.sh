#!/bin/sh

pip install -r requirements.txt
if [ "$1" != "" ]
  then
    echo $*
    python manage.py syncdb
    python import.py $1
fi
python manage.py syncdb
python manage.py runserver
