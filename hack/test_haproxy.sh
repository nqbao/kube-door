#!/bin/bash

# a quick script to test on local

mkdir -p conf
HACONFIG=$(cd .. && python -m kube_door)
echo "$HACONFIG" > conf/haproxy.cfg
docker run --rm --net=host -v `pwd`/conf:/usr/local/etc/haproxy haproxy
