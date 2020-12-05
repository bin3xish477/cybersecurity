
# Should take 5-6 minutes to build

# Instruction to run:
#   docker build -t pentest_image
#   docker run -d -p 8834:8834 --name red_team_container pentest_image
#   docker exec -it pentest_image

# Currently installes:
# - metasploit
# - gobuster
# - nmap
# - whatweb
# - john
# - netcat
# - vim
# - nishang
# - seclists
# - sqlmap
# - Nessus


FROM ubuntu

LABEL maintainer="rodriguez10011999@gmail.com"
LABEL version="0.1"
LABEL description="A basic docker container based on Ubuntu for practicing your pentest skills"

RUN apt update && \
    apt upgrade && \
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

RUN wget https://golang.org/dl/go1.15.6.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz && \
    rm ./go1.15.6.linux-amd64.tar.gz 

RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc

# Setup Metasploit
RUN wget https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb -O ./msfinstall

RUN chmod +x msfinstall && \
    ./msfinstall && \
    rm ./msfinstall

RUN apt install -y nmap && \
    apt install -y whatweb && \
    apt install -y john && \
    apt install -y netcat && \
    apt install -y vim 

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
#RUN wget 'https://github.com/sqlmapproject/sqlmap/tarball/master' -O /opt/sqlmap.tar.gz && \
    #tar -xzf /opt/sqlmap.tar.gz -C /opt && \
    #find /opt -name "sqlmap*" -type d | xargs -I {} ln -s '{}/sqlmap.py' /bin/sqlmap


# Setup Nessus
# Nessus-8.12.1-debian6_amd64.deb checksum : b878e1b85b4c8aa04d4a579059c88fbca216e8fa64da9f60207ce28a204b7d68

ADD Nessus-8.12.1-debian6_amd64.deb /tmp/Nessus-8.12.1-debian6_amd64.deb

RUN dpkg -i /tmp/Nessus-8.12.1-debian6_amd64.deb && \
    rm -r /tmp/Nessus-8.12.1-debian6_amd64.deb
    
# https://localhost:8834
EXPOSE 8834

CMD service nessusd start && tail -f /dev/null


    
