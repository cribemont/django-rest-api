FROM python:alpine3.13
MAINTAINER C.Ribemont

# Stabilise python on docker
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# User to run app process only and avoir root usage
RUN adduser -D user
USER user