FROM ubuntu:16.04

ADD docker/setup.sh /tmp
RUN /tmp/setup.sh

ADD requirements.txt /opt/kube-door/
RUN pip install --no-cache-dir -r /opt/kube-door/requirements.txt
ADD kube_door /opt/kube-door/kube_door
ADD docker/bootstrap.sh /opt/bootstrap.sh

CMD ["/opt/bootstrap.sh"]
