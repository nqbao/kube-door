#!/bin/bash

set -e

echo "Generating haproxy config ..."
(
  cd /opt/kube-door
  python -m kube_door > /etc/haproxy/haproxy.cfg
)

echo "Running haproxy ..."
exec haproxy -f /etc/haproxy/haproxy.cfg -p /var/run/haproxy.pid
