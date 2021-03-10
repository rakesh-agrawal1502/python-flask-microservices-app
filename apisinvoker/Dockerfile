# Used for building docker image for home service
# docker build -f Dockerfile -t rakeshagrawal1502/python-flask-apisinvoker:1.0 .
# docker image push rakeshagrawal1502/python-flask-apisinvoker:1.0

FROM rakeshagrawal1502/python-flask-service:1.1
WORKDIR /usr/src/app
ADD . /usr/src/app
CMD ["python3","invokeapis.py"]