#!/usr/bin/env bash
if type -t move &>/dev/null
then
    printf "Windows\n"
elif type -t scutil &>/dev/null
then
    printf "MAC OS\n"
else
    printf "Linux\n"
fi
