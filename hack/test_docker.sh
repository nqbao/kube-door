#!/bin/bash

docker run --rm -it \
  -v ~/.kube:/kubeconfig \
  -e KUBECONFIG=/kubeconfig/config \
  --net=host \
  --name=kube-door kube-door
