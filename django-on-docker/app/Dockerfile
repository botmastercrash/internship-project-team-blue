FROM python:3-alpine
WORKDIR /usr/scr/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DJANGO_ALLOWED_HOSTS
ARG SECRET_KEY
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .