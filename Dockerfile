FROM ubuntu

LABEL maintainer="rodriguez10011999@gmail.com"
LABEL version="0.1"
LABEL description="A basic docker container based on Ubuntu for practicing your pentest skills"

RUN apt update && \
    apt upgrade && \
    echo "12\n5\n" | apt install -y golang && \
    apt install -y git && \
    apt install -y python3 && \
    apt install -y python3-pip

RUN echo 'export GOROOT=/usr/local/go' >> ~/.bashrc && \
    echo 'export GOPATH=$HOME/go' >> ~/.bashrc && \
    echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.bashrc

#RUN apt install -y setoolkit && \
    #apt install -y gobuster && \
    #apt install -y nmap && \
    #apt install -y whatweb && \
    #apt install -y metasploit && \
    #apt install -y john
    #apt install -y netcat && \
    #apt install -y seclists && \
    #apt install -y nishang && \
    #apt install -y apache2 && \
    #apt install -y vim

CMD ["echo", "Welcome", "to", "my", "Pentesting", "Docker", "Image"]
    
    
