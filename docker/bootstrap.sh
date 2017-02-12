#!/bin/bash

set -e

(
  cd /opt/kube-door
  python -m kube_door > /etc/haproxy/haproxy.cfg
)

exec haproxy -f /etc/haproxy/haproxy.cfg -p /var/run/haproxy.pid
