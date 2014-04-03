#!/bin/bash

if [ `which virtualenv` != "" ]
  then
    if [ ! -d ".venv" ]
      then
        virtualenv .venv
    fi
    source .venv/bin/activate
fi

pip install -r requirements.txt
if [ "$1" != "" ]
  then
    python manage.py syncdb
    python import.py $1
fi
python manage.py syncdb
python manage.py runserver 0.0.0.0:8000
