FROM python:3.6
LABEL maintainer="jpm"
LABEL version="0.1"
LABEL description="NLP API demo image"

ARG BUILD_DATE

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# required modules
RUN python -m spacy download en_core_web_sm
RUN python -c "import nltk; nltk.download('punkt')"

COPY . /usr/src/app

ENV PYTHONPATH=.:/usr/src/app

EXPOSE 8000

CMD ["gunicorn", "--config", "gunicorn.conf", "--log-config", "logging.conf", "wsgi:app"]
