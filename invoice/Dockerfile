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
CMD ["gunicorn","-b","0.0.0.0:8000", "run"]
# Below is for default server
# CMD ["python","run.py","-h", "0.0.0.0"]