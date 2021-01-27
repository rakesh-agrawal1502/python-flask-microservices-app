# This will create a base image using which individual service images will be created
# docker build -f Dockerfile -t rakeshagrawal1502/python-flask-service:1.0 .
# docker image push rakeshagrawal1502/python-flask-service:1.0

FROM python:3.7
RUN apt-get update -y
RUN apt-get install vim -y
RUN apt-get install net-tools -y
RUN apt-get install apt-utils -y
RUN pip install --upgrade pip
RUN pip install gunicorn
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt