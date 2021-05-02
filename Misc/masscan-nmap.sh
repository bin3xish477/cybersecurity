#!/bin/bash

# Automating Masscan/Nmap initial reconnaissance workflow
# for cloud pentesting. However, this could obviously be used for 
# any engagement

IP_FILE=$1
INTERFACE=$2

if [ -n IP_FILE ]; then
    echo "usage: $0 <interface-name> <ip-file>"
    exit 1
fi

PORT_LIST="7,9,13,21-23,25-26,37,53,79-81,88,106,110-111,113,119,135,139,143-144,179,199,389,427,443-445,465,513-515,543-544,548,554,587,631,646,873,990,993,995,1025-1029,1110,1433,1720,1723,1755,1900,2000-2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000-6001,6379,6646,7070,8000,8008-8009,8080-8081,8443,8888,9100,9999-10000,27017,32768,49152-49157"


masscan -iL -p $PORT_LIST --adapter $INTERFACE -oG temp.out

grep 'Host' temp.out | \
    awk '{print $5}' | \
    awk -F/ '{print $1}' | \
    grep [0-9] | \
    sort -u | \
    tr '\n' ',' | \
    sed 's/,$//' > ports

nmap -iL $IP_FILE -p $(cat ports) -A -Pn -oA nmap-$(date '+%Y%m%d%M%S')-1
