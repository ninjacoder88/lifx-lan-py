FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/py/

COPY *.sh /app/sh/

RUN pip install --no-cache-dir -r py/requirements.txt

RUN django-admin startproject lifxapp

RUN apt-get update && apt-get install -y dos2unix

EXPOSE 8000

RUN dos2unix ./sh/startup.sh

CMD ["/bin/sh", "./sh/startup.sh"]