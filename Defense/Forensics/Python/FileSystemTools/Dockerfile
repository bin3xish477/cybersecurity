FROM ubuntu

RUN sudo apt update && \
    yes | sudo apt upgrade && \
    sudo apt install python3 && \
    sudo apt install python3-pip && \
    sudo pip3 install colored

RUN mkdir /binexistools

COPY . /binexistools

CMD ["ls", "/binexistools"]


