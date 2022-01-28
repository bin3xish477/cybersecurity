#!/usr/bin/env bash

####################################################
Quick script to run gobuster against files with urls
using the common options I use with gobuster
####################################################

URL_FILE=$1
WORDLIST=$2
THREADS=$3
ERROR_CODES=$4

for url in $(cat $URL_FILE);
do

  echo "==> $url"

  if [[ -z $ERROR_CODES ]];
  then
    ERROR_CODES=404
  fi

  if [[ -z $THREADS ]];
  then
    THREADS=15
  fi

  IP=$(echo $url | egrep -o '([0-9]{1,3}\.){3}[0-9]{1,3}')

  gobuster dir -u $url -w $WORDLIST -q -k -r -t $THREADS -b $ERROR_CODES --timeout 10s --no-error --useragent "$GOOGLEBOT" | tee $IP-gobuster.stdout
done
