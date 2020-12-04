FROM ubuntu

LABEL maintainer="rodriguez10011999@gmail.com"
LABEL version="0.1"
LABEL description="A basic docker container based on Ubuntu for practicing your pentest skills"

RUN apt update && \
    apt upgrade && \
    apt install -y git && \
    apt install -y python3 && \
    apt install -y python3-pip && \
    apt install -y ruby-full && \
    apt install -y wget && \
    apt install -y net-tools && \
    apt install -y iputils-ping && \
    apt install -y iproute2

RUN wget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz && \
    rm ./go1.15.6.linux-amd64.tar.gz 

RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc

RUN wget https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb -O ./msfinstall

RUN chmod +x msfinstall && \
    ./msfinstall && \
    rm ./msfinstall

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


# Install Nessus

# SHA256 checksum : b878e1b85b4c8aa04d4a579059c88fbca216e8fa64da9f60207ce28a204b7d68
# Download directory from Nessus download page : https://www.tenable.com/downloads/nessus

# https://locatlhost:8834
RUN wget https://github.com/binexisHATT/EthicalHacking/raw/master/Nessus-8.12.1-debian6_amd64.deb && \
    dpkg -i Nessus*.deb && \
    rm Nessus.deb

CMD ["echo", "Happy", "Hacking !!!", "&&", "systemctl", "start", "nessusd.service"]
    
    
