FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN django-admin startproject mysite

RUN apt-get update && apt-get install -y dos2unix

EXPOSE 8000

#CMD [ "python ./mysite/manage.py runserver" ] 

#COPY *.py /app/lifx/
COPY *.sh /app/demo/

#EXPOSE 8000

RUN dos2unix ./demo/startup.sh

CMD ["/bin/sh", "./demo/startup.sh"]