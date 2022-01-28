#!/usr/bin/env bash

#### Run
# openvpn --script-security 2 --down fail_safe_openvpn.sh --config [OPENVPN_CONFIG_FILE]

echo '==> disabling network...'
systemctl stop network-manager
killall -9 dhclient

for i in $(ifconfig | grep -Eio '^[a-z0-9]+:' | grep -v '^lo:$' | cut -d':' -f1)
do
  ifconfig $i 0.0.0.0 down
done
