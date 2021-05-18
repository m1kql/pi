# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
LABEL maintainer="yak-fumblepack"
# update system
RUN set -eux; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  ca-certificates \
  netbase \
  ; \
  rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -U -r requirements.txt

COPY . . 

CMD ["python", "main.py"]


