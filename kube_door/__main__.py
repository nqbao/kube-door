import argparse
import time
import sys
import subprocess

from .generator import get_exposed_ports, get_node_ips, render_haproxy

parser = argparse.ArgumentParser(description="Kube-Door command line")
# TODO: add a flag to output to a file
parser.add_argument("--output", required=False, help="Path to output haproxy config content")
parser.add_argument("--auto-update", action='store_true', required=False,
                    help="Watch for changes and update the config file automatically")

args = parser.parse_args()

content = render_haproxy(get_exposed_ports(), get_node_ips())

if args.output:
    def write_to_output(content):
        with open(args.output, "w") as f:
            print "Updating %s ..." % args.output
            f.write(content)

    if args.auto_update:
        prev_content = None
        retries = 0
        print "Watching for changes ..."
        while True:
            try:
                content = render_haproxy(get_exposed_ports(), get_node_ips())
                retries = 0

                if content != prev_content:
                    write_to_output(content)
                    prev_content = content

                    # Only support this for now
                    subprocess.check_call(["service", "haproxy", "restart"])
            except Exception as ex:
                print "Unable to fetch config"
                print ex
                retries += 1

                if retries > 10:
                    sys.exit(1)

            time.sleep(10)
    else:
        write_to_output(content)

else:
    print content
