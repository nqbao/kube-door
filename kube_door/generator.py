import os
import kubernetes.client
import kubernetes.config
import jinja2


# read config from KUBECONFIG environment
if os.environ.get('KUBECONFIG'):
    kubernetes.config.load_kube_config(os.environ.get('KUBECONFIG'))
else:
    # behave like kubectl
    kubernetes.client.configuration.host = "http://localhost:8080"


def _get_ip(node):
    ip = None

    for address in node.status.addresses:
        if not ip or address.type == 'InternalIP':
            ip = address.address

    return ip


def get_node_ips():
    client = kubernetes.client.CoreV1Api()
    nodes = client.list_node().items
    return map(_get_ip, nodes)


def get_exposed_ports():
    client = kubernetes.client.CoreV1Api()
    services = client.list_service_for_all_namespaces().items
    ports = {}

    for service in services:
        if not service.metadata.annotations or 'kube-door/ports' not in service.metadata.annotations:
            continue

        exposed_ports = service.metadata.annotations['kube-door/ports'].split(',')
        hostname = service.metadata.annotations.get('kube-door/hostname', None)

        for port in service.spec.ports:
            if not port.node_port or str(port.port) not in exposed_ports:
                continue

            if port.port not in ports:
                ports[port.port] = []

            ports[port.port].append({
                'hostname': hostname,
                'name': service.metadata.name,
                'namespace': service.metadata.namespace,
                'node_port': port.node_port
            })

    return ports


def render_haproxy(ports, ips):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('kube_door')
    )
    return env.get_template('haproxy.cfg.jinja2').render(ports=ports, ips=ips)
