
import requests
import argparse


def check_url():
    url = "http://localhost"
    for i in range(1,100):
        r=requests.get(url)
        #print(r)
        print("HTTP/1.1 %s %s"%(r.status_code,r.reason))

check_url()
