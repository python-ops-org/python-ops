#!/usr/bin/env python

import argparse
import json
import os
import sys
import time

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

AWS_SITE_YAML_FILE = 'site.yml'
CFG_KEY_URLS_LIST = 'urls-list'

CHROME_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'

PING_METHOD = 'icmp'  # methods are: 'url' or 'icmp'


def error(msg, and_exit=True):
    print("ERROR: %s" % msg)
    if and_exit:
        sys.exit(-1)

try:
    import pyping
    import requests
    import yaml
except ImportError as ie:
    LIB_MAP = {'yaml': 'PyYAML'}
    m = ie.message
    missing_mod = m[m.rfind(" "):].strip()
    error("missing python module '%s' (please install manually)" % missing_mod, and_exit=False)
    print("  use: pip install %s" % LIB_MAP.get(missing_mod, missing_mod))
    sys.exit(-1)


def get_urls_from_file(yaml_file):
    if not os.path.isfile(yaml_file):
        error("yaml file not exists: %s" % yaml_file)
    with open(yaml_file) as f:
        y = yaml.load(f)
        if CFG_KEY_URLS_LIST not in y:
            error("missing yaml config entry '%s' in '%s'" % (CFG_KEY_URLS_LIST, yaml_file))
        return y[CFG_KEY_URLS_LIST]


def _ping_url(url):
    start = time.time()
    response = requests.get(url, headers={'User-Agent': CHROME_USER_AGENT})
    elapsed = time.time() - start
    return elapsed * 1000


def _ping_icmp(url):
    hostname = urlparse(url).hostname
    p = pyping.ping(hostname)
    if p.ret_code != 0:
        raise Exception(p.output[1])
    return float(pyping.ping(hostname).avg_rtt)


def ping(url):
    if PING_METHOD == 'url':
        return _ping_url(url)
    elif PING_METHOD == 'icmp':
        return _ping_icmp(url)
    else:
        raise NotImplementedError("unknown PING_METHOD: %s" % PING_METHOD)


def lambda_handler(event, context):
    result = []
    for url in get_urls_from_file(AWS_SITE_YAML_FILE):
        try:
            result.append({'url': url, 'pinged': "%0.fms" % ping(url)})
        except Exception as exc:
            result.append({'url': url, 'pinged': "error: %s" % exc})
    return json.dumps(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('YAML_FILE', help="yaml file containing the list of urls to ping")
    args = parser.parse_args()

    for url in get_urls_from_file(args.YAML_FILE):
        try:
            print("%0.fms pinging %s" % (ping(url), url))
        except Exception as exc:
            print("error pinging '%s': %s" % (url, exc))


if __name__ == '__main__':
    main()
