FROM ubuntu:latest

RUN apt update && \
    apt -y upgrade && \
    apt install -y python3 && \
    apt install -y python3-pip

RUN mkdir -p /opt/Pyphish

COPY . /opt/Pyphish/

RUN pip3 install -r /opt/Pyphish/requirements.txt

