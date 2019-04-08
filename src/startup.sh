#!/bin/bash
python ./mysite/manage.py migrate
python ./mysite/manage.py runserver 0:8000