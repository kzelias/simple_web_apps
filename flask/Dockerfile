FROM python:3.9-alpine

RUN apk update && pip install -U pip
#apt-get update for non-alpine image

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./app.py ./app.py

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]