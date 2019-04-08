FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN django-admin startproject lifxapp

RUN apt-get update && apt-get install -y dos2unix

EXPOSE 8000

COPY *.sh /app/demo/

RUN dos2unix ./demo/startup.sh

CMD ["/bin/sh", "./demo/startup.sh"]