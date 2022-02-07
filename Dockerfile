FROM python:3.8.10
MAINTAINER Dineshkumar Dhayalan
ADD . ./app
WORKDIR /app
RUN pip install -r requirements.txt
