#!/usr/bin/env bash

python3 dfsc.py -w 3 -a md5 . &

sleep 1
touch ./{1..20}.txt

for i in $(seq 1 20)
do
    echo "Hello" > ./$i.txt
done

exit 0
