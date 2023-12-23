#!/usr/bin/python

#!/usr/bin/python3

import argparse
import re
import subprocess
import sys

def is_port_used(port):
    cmd = 'netstat -ntlp | grep "%s"' % port
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, _ = p.communicate()

    # Decode the bytes to string using UTF-8
    out_str = out.decode('utf-8')

    matches = re.findall("^[\w\d\s\.:]+:(%s)\s+.*$" % port, out_str, re.MULTILINE)
    return True if matches else False

def main():
    parser = argparse.ArgumentParser(description="testing")
    parser.add_argument('-p', '--port', dest='port', default='80', help='port to check')
    args = parser.parse_args()

    try:
        port = int(args.port)
    except ValueError:
        print("error: Invalid port number")
        sys.exit(-1)

    if is_port_used(args.port):
        print("ok: Port {} is in use".format(port))
    else:
        print("not ok: Port {} is not in use".format(port))

if __name__ == '__main__':
    main()

