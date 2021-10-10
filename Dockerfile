FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . ./
COPY ./requirements.txt /requirements.txt
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install wheel
RUN apk add --no-cache python3-dev libffi-dev gcc 
RUN pip install -r /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
