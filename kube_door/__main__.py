import argparse

from .generator import get_exposed_ports, get_node_ips, render_haproxy

parser = argparse.ArgumentParser(description="Kube-Door command line")
# TODO: add a flag to output to a file
parser.add_argument("--output", required=False, help="Path to output haproxy config content")

args = parser.parse_args()

content = render_haproxy(get_exposed_ports(), get_node_ips())

if args.output:
    with open(args.output, "w") as f:
        f.write(content)
else:
    print content
