#!/usr/bin/env bash

#IFS=$"\n"
if [[ $EUID != "0" ]]
then
    echo "[-] Must run $0 as root..."
    exit 1
fi

printf "%15s\n" "Date"
printf "========================================================================================\n"

while read LINE 
do
    [[ -z $LINE ]] && continue
    if [[ "$LINE" == *"COMMAND"* ]] && [[ "$LINE" == *"PWD"* ]]
    then
        DATE=$(echo $LINE | egrep -o '[JFMASONDa-z]{3}\s[0-9]{1,2}\s[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}')
        USERNAME=$(echo $LINE | egrep -o 'USER=[A-Za-z0-9]+\s')
        DIRECTORY=$(echo $LINE | grep -Po 'PWD=.*\s' | cut -d ";" -f1)
        echo $DATE $USERNAME $DIRECTORY
    else
        continue
    fi
done < /var/log/auth.log

