#!/usr/bin/env bash

echo '==> disabling network...'
systemctl stop network-manager
killall -9 dhclient

for i in $(ifconfig | grep -Eio '^[a-z0-9]+:' | grep -v '^lo:$' | cut -d':' -f1)
do
  ifconfig $i 0.0.0.0 down
done
