
import requests
import argparse
import json
import csv
from bs4 import BeautifulSoup
import re

#span class="ansi33"

token = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
headers = {"Content-Type": "application/json", "Authorization": "Bearer %s"%token}

def work():
	name = ""
	fo = open("t2.json","r")
	data_2 = json.load(fo,strict=False)
	extra_vars = json.loads(data_2["extra_vars"])
	nex_url = "not_present"
	try:
		nex_url = extra_vars["nexus_url"]
	except:
		nex_url = "not present"
	#print(extra_vars)
	print(nex_url)
work()
