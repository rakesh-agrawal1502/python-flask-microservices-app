# Used for building docker image for home service
# docker build -f Dockerfile -t rakeshagrawal1502/python-flask-home:1.0 .

FROM rakeshagrawal1502/python-flask-service:1.0
WORKDIR /usr/src/app
ADD . /usr/src/app
CMD ["gunicorn","-b","0.0.0.0:8000", "run"]