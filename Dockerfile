FROM ubuntu:20.04

#python:3.9.15-bullseye

# setup environment variable  

ENV PORT=8000
ENV DEBIAN_FRONTEND=noninteractive
# set environment variables  

# Can uncomment if you don't want pyc created in containers 
ENV PYTHONDONTWRITEBYTECODE 1

# Send  stderr and stdout direct to logs without buffering
# Also prevent waiting on Watching for file changes with StatReloader issue
ENV PYTHONUNBUFFERED 1  


COPY . /app

WORKDIR /app

RUN env 
RUN echo $REDIS_HOST
#RUN azfsadfsdgfdszg
# install dependencies
RUN apt-get update
RUN apt-get -y install python3.9
RUN apt-get -y install python3-pip
RUN apt-get -y install build-essential
RUN apt-get -y install  libpython3.9-dev

RUN python3.9 -m pip install --upgrade pip  
RUN python3.9 -m pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python3.9 manage.py migrate && python3.9 manage.py runserver "0.0.0.0:$PORT"