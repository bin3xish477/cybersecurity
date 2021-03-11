#!/bin/bash
DIR="$HOME/Downloads"

if [ -f "$HOME/virus-scan.log" ]
then
    rm ${HOME}/virus-scan.log
fi

IFS=$(echo -en "\n\b")

shopt -s lastpipe
inotifywait --quiet --monitor --event create --recursive --format '%w%f' $DIR | while read FILE
sleep 1s
do
    if [ -s $FILE ]; then
         date > $HOME/virus-scan.log
         clamdscan --move=$HOME/virus-quarantine $FILE >> $HOME/virus-scan.log
         kdialog --title "Virus scan of $FILE" --msgbox "$(cat $HOME/virus-scan.log)"
    fi
done 
