FROM ubuntu:24.04

ENV PYTHONUNBUFFERED 1
ENV LC_ALL=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y install \
      build-essential \
      gcc \
      python3-venv \
      python3-dev \
      libffi-dev \
      libpq-dev  \
      libssl-dev \
      gettext \
      git \
    && \
    apt-get clean && \
    mkdir /app && \
    useradd -m app

WORKDIR /app

USER app

ADD requirements-test.txt /app/

ENV PATH /home/app/venv/bin:${PATH}

RUN python3 -m venv ~/venv && \
    pip install --upgrade pip && \
    pip install -r requirements-test.txt && \
    pip install Django==5.0.6

ADD . /app/

ENV DJANGO_SETTINGS_MODULE tests.settings
