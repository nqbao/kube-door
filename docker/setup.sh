#!/bin/bash

apt-get update && apt-get install -y --no-install-recommends haproxy python-pip python-setuptools
pip install --upgrade pip==9.0.1

# clean up
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*
