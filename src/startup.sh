#!/bin/bash
python ./lifxapp/manage.py migrate
python ./lifxapp/manage.py runserver 0:8000