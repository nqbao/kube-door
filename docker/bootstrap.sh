#!/bin/bash

set -e

echo "Generating haproxy config ..."
cd /opt/kube-door
python -m kube_door --output /etc/haproxy/haproxy.cfg --auto-update &
wait
