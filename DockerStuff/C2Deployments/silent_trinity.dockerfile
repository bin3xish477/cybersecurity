#############################
# build with:
# docker build -t silent --build-arg TS_PASS=YourSecurePassPhrase -f ./silent_trinity.dockerfile .
# run with:
# docker run --name silent -d -v /opt/st:/root/st/data -p 5000:5000 silent
##############################
# connect to server from Kali with:
# python3 st client wss://sername>:<teamserver_password>@<teamserver_ip>:5000
##############################

FROM python:3.7.11-slim-stretch
ARG TS_PASS
ENV TS_PASS=$TS_PASS
RUN apt update && apt install -y git make gcc
RUN git clone https://github.com/byt3bl33d3r/SILENTTRINITY/ /root/st/
WORKDIR /root/st/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT python st.py teamserver 0.0.0.0 $TS_PASS
