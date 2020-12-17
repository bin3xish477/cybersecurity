#!/usr/bin/env bash

echo "[+] Adding pycook dir to PATH variable ..."
if [[ "$SHELL" == "/bin/bash" ]];
then
  echo "export PATH=$PATH:$(pwd)" >> ~/.bashrc
elif "$SHELL" == "/bin/zsh" ]]
then
  echo "export PATH=$PATH:$(pwd)" >> ~/.zshrc
fi
echo "[ OK ]"

echo "[+] Installing Python3 dependies with pip3 ..."
pip3 install -r requirements.txt
echo "[ OK ]"

