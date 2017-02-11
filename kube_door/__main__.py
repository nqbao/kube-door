from .generator import get_exposed_ports, get_node_ips, render_haproxy

print render_haproxy(get_exposed_ports(), get_node_ips())
