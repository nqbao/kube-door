#!/bin/bash

mkdir -p conf
python -m kube_door > conf/haproxy.cfg
docker run --rm --net=host -v `pwd`/conf:/usr/local/etc/haproxy haproxy
