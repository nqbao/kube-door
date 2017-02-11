#!/bin/bash

python -m kube_door > conf/haproxy.cfg
docker run --rm -p 80:80 -v `pwd`/conf:/usr/local/etc/haproxy haproxy
