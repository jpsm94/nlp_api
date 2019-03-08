FROM python:3-alpine
# MAINTAINER  JPM

ARG BUILD_DATE
ARG VCS_REF

# Set labels (see https://microbadger.com/labels)
#LABEL org.label-schema.build-date=$BUILD_DATE \
#      org.label-schema.vcs-ref=$VCS_REF \
#      org.label-schema.vcs-url="https://github.com/nikos/rest_api_demo"


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV PYTHONPATH=.:/usr/src/app

EXPOSE 8000

CMD cd /usr/src/app && python nlp_api/app.py
