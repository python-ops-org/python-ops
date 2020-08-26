import csv
import json
import argparse
import requests
import re
from datetime import datetime
from requests.auth import HTTPBasicAuth
import re



def hosts():
        headers = {'Content-Type': 'application/json','Authorization':'Bearer UZj22SwyfG3LdUYELJlzd65f4gzFBZ' }
        r = requests.get('http://192.168.56.159/api/v2/hosts', headers=headers)
        data = json.loads(r.text)
        print(data)


hosts()              
