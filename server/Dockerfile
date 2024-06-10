FROM python:3.11.3-alpine3.16

ENV LANG C.UTF-8

RUN apk update
RUN apk add --virtual build-deps gcc g++ musl-dev && \
    apk add postgresql-dev

RUN mkdir -p /src/app
WORKDIR /src/app

ENV PYTHONPATH=/src/app:/src/app/src

COPY requirements.txt .
RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt
