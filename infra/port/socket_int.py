#!/usr/bin/python3

import argparse
import socket
import sys

def is_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Adjust the timeout as needed

    try:
        sock.connect(('127.0.0.1', port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="testing")
    parser.add_argument('-p', '--port', dest='port', type=int, default=80, help='port to check')
    args = parser.parse_args()

    if is_port_open(args.port):
        print(f"ok: Port {args.port} is open")
    else:
        print(f"not ok: Port {args.port} is not open")

if __name__ == '__main__':
    main()
