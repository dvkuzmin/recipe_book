FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./recipe /app
