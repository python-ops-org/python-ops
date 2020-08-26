
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
	fo = open("job-t1.json","r")
	data_2 = json.load(fo,strict=False)
	tmp = data_2["extra_vars"].split("\n")
	nex_url = "not_present"
	em = "not_present"
	try:
		nex_url = json.loads(data_2["extra_vars"])["nexus_url"]
		em = str(tmp[2].split(":")[1].replace('"',"")).replace(" ","")
	except:
		nex_url = "not present"
		em = "not_present"
	print(nex_url)
    






work()
