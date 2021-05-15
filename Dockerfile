# Should take 5-6 minutes to build

# Instruction to run:
#   docker build -t pentest
#   docker run -d -p 8834:8834 --name red pentest
#   docker exec -it red /bin/bash

# Currently installes:
# - metasploit
# - gobuster
# - masscan
# - nmap
# - whatweb
# - john
# - socat
# - netcat
# - vim
# - nishang
# - seclists
# - sqlmap
# - impacket
# - awscli
# - az (azure cli)
# - pacu
# - ffuf
# - wpscan

FROM ubuntu

LABEL maintainer="rodriguez10011999@gmail.com"
LABEL version="0.1"
LABEL description="A basic docker container based on Ubuntu for pentesting"

RUN apt update && apt upgrade && \
    apt install -y git && \
    apt install -y python3 python && \
    apt install -y python3-pip && \
    apt install -y ruby-full && \
    apt install -y wget && \
    apt install -y net-tools && \
    apt install -y iputils-ping && \
    apt install -y iproute2 && \
    apt install -y p7zip-full p7zip-rar && \
    apt install -y apt-utils && \
    DEBIAN_FRONTEND="noninteractive" apt install -y tzdata
# golang
RUN wget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz && \
    rm ./go1.15.6.linux-amd64.tar.gz 
RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc

# Setup Metasploit
RUN wget https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb -O ./msfinstall && \
    chmod +x msfinstall && \
    ./msfinstall && \
    rm ./msfinstall

# nmap whatweb john netcat vim masscan socat
RUN apt install -y nmap whatweb john netcat vim masscan socat

# Setup Gobuster
# SHA256 Checksum : 7f11cba97772ac4f276177d5d782e6ebda58fbdbbbf959d6cb02e0454bc52e14
RUN wget https://github.com/OJ/gobuster/releases/download/v3.1.0/gobuster-linux-amd64.7z -O /opt/gobuster-linux-amd64.7z && \
    7z e /opt/gobuster-linux-amd64.7z -o/opt/ && \
    rm /opt/gobuster-linux-amd64.7z && \
    rm -rf /opt/gobuster-linux-amd64 && \
    chmod +x /opt/gobuster && \
    mv /opt/gobuster /bin/gobuster

# Setup Waybackurls
RUN git clone https://github.com/tomnomnom/waybackurls.git /opt/waybackurls && \
    ln -s /opt/waybackurls/main.go /bin/waybackurls
# Setup Nishang
RUN git clone https://github.com/samratashok/nishang.git /opt/nishang
# Setup Seclists
RUN git clone https://github.com/danielmiessler/SecLists.git /opt/SecLists
# Setup Sqlmap
RUN wget 'https://github.com/sqlmapproject/sqlmap/tarball/master' -O /opt/sqlmap.tar.gz && \
    tar -xzf /opt/sqlmap.tar.gz -C /opt && \
    find /opt -name "sqlmap*" -type d | xargs -I {} ln -s '{}/sqlmap.py' /bin/sqlmap  
# chisel
RUN mkdir /opt/chisel && https://github.com/jpillora/chisel/releases/download/v1.7.6/chisel_1.7.6_linux_amd64.gz -O /opt/chisel/
# impacket
RUN git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket && pip install -r /opt/impacket/requirements.txt
# aws cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install && rm -rf awscliv2.zip aws
# azure cli
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
# pacu
RUN pip install -U pacu
# ffuf
RUN git clone https://github.com/ffuf/ffuf /opt/ffuf; cd /opt/ffuf ; go get && go build
