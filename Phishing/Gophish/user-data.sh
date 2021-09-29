#!/bin/bash

gophish_setup() {
  mkdir /opt/gophish
  cd /opt/gophish
  wget -O gophish.zip 'https://github.com/gophish/gophish/releases/download/v0.11.0/gophish-v0.11.0-linux-64bit.zip'
  unzip gophish.zip
  rm gophish.zip
  sed -i 's|127\.0\.0\.1|0\.0\.0\.0|g' config.json
  chmod +x ./gophish
  ./gophish &
}

mailhog_setup() {
  # Use mailhog as the sending SMTP server
  mkdir /opt/mailhog
  cd /opt/mailhog
  wget -O mailhog 'https://github.com/mailhog/MailHog/releases/download/v1.0.1/MailHog_linux_amd64'
  chmod +x ./mailhog
  ./mailhog &
}

gophish_setup
mailhog_setup
