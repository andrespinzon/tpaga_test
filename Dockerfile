FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

ADD . /tpaga_test
WORKDIR /tpaga_test

RUN pip install --upgrade pip

COPY requirements.txt /tpaga_test/
RUN pip install -r requirements.txt
COPY . /tpaga_test/