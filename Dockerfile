FROM python:3.6-alpine

WORKDIR /app

ADD requirements.txt /app

#VOLUME /app

#ENV FLASK_APP=app.py
#ENV FLASK_ENV=development

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    zlib-dev \
    make \
    libc-dev \
    && pip --no-cache-dir install --upgrade pip \
    && pip --no-cache-dir install -r requirements.txt \
    && apk del .build-deps

#EXPOSE 5000

#CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]

