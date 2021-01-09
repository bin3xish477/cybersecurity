#!/usr/bin/env bash

$TARGET=$1
# Make nmap directory if it doesn't exist
[[ ! -d nmap ]] && mkdir nmap

# Perform port scan against all tcp ports
nmap -Pn -p- -oN nmap/all_ports.txt $TARGET

# Filter ports from all ports scan for only open TCP ports
$OPEN_PORTS=$(cat nmap/all_ports.txt | egrep -oE '([0-9]+)/tcp' | \
    awk -F/ '{print $1}' | \
    tr "\n" "," | rev | cut -c 2- | rev)

# Pass extracted open ports into an nmap with service scan
# and default scripts enabled
nmap -sV -sC -p $OPEN_PORTS -oN nmap/service_enum.txt $TARGET
