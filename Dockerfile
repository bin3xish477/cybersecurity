FROM ubuntu:20.4

RUN sudo apt update && \
    sudo apt upgrade && \
    sudo apt install -y golang

RUN echo 'export GOROOT=/usr/local/go \
    export GOPATH=$HOME/go \
    export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> .bashrc

RUN sudo apt install -y setoolkit && \
    sudo apt install -y gobuster && \
    sudo apt install -y nmap && \
    sudo apt install -y whatweb && \
    sudo apt install -y metasploit && \
    sudo apt install -y python3 && \
    sudo apt install -y python3-pip

CMD ["Welcome", "to", "my", "Pentesting", "Docker", "Image"]
    
    
