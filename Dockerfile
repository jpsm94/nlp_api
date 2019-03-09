FROM python:3.6
LABEL maintainer="jpm"
LABEL version="0.1"
LABEL description="Demo image"

ARG BUILD_DATE
ARG VCS_REF

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . /usr/src/app

ENV PYTHONPATH=.:/usr/src/app

EXPOSE 8000

CMD cd /usr/src/app/ && gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
