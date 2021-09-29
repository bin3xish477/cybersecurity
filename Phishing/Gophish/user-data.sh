#!/bin/bash

mkdir /opt/gophish
cd /opt/gophish
wget -O gophish.zip https://github.com/gophish/gophish/releases/download/v0.11.0/gophish-v0.11.0-linux-64bit.zip
unzip gophish.zip
sed -i 's|127\.0\.0\.1|0\.0\.0\.0|g' config.json
chmod +x ./gophish
./gophish

