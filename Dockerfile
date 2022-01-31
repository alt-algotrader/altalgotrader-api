FROM python:3.8
MAINTAINER Alt "alt.algotrader@gmail.com"
RUN apt-get update -y
RUN apt-get install gcc musl-dev
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install cython
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install p5py PEP517
RUN pip3 install -r requirements.txt