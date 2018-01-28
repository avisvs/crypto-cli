FROM python:3.6.4-alpine3.6

LABEL maintainer sjbitcode@gmail.com

RUN mkdir /crypto-app
WORKDIR /crypto-app

COPY requirements.txt /crypto-app
RUN pip install -r requirements.txt

ADD . /crypto-app

ENTRYPOINT [ "python", "./main.py" ]
