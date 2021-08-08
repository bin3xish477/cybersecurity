FROM golang:latest

RUN apt update && apt upgrade -y && \
  apt install wget tar -y

RUN go get -v -u github.com/tomnomnom/fff
RUN go get -v -u github.com/tomnomnom/assetfinder
RUN go get -v -u github.com/tomnomnom/gron
RUN go get -v -u github.com/tomnomnom/gf
RUN go get -v -u github.com/tomnomnom/httprobe
RUN go get -v -u github.com/tomnomnom/unfurl
RUN go get -v -u github.com/tomnomnom/anew
RUN go get -v -u github.com/tomnomnom/waybackurls
RUN go get -v -u github.com/OWASP/Amass/v3/...
RUN go get -u github.com/ffuf/ffuf

WORKDIR /tools
RUN wget https://github.com/epi052/feroxbuster/releases/download/v2.3.2/x86_64-linux-feroxbuster.tar.gz && \
  tar xzvf x86_64-linux-feroxbuster.tar.gz && chmod +x feroxbuster && \
  install feroxbuster /usr/local/bin/feroxbuster && rm ./x86_64-linux-feroxbuster.tar.gz
