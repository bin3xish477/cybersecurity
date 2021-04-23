#!/bin/bash
SSH_FILE=$1
sed -e "s/-----BEGIN OPENSSH PRIVATE KEY-----/&\n/"\
    -e "s/-----END OPENSSH PRIVATE KEY-----/\n&/"\
    -e "s/\S\{64\}/&\n/g"\
    $SSH_FILE
