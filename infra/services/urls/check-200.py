import requests
from requests.exceptions import RequestException
import argparse

def check_url():
    try:
        url = "http://localhost"
        r=requests.get(url, verify=False)
        if r.status_code == requests.status_codes.codes.ok:
            print("%s %s ok" %(url, r.status_code))
    except RequestException as error:
        print("%s is not reachable\n%s"%(url, error))

check_url()
