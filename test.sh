#!/bin/bash

python -m kube_door > conf/haproxy.cfg
docker run --rm -p -net host -v `pwd`/conf:/usr/local/etc/haproxy haproxy
