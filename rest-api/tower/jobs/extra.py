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
	cr = ""
	em = ""
	try:
		cr = str(tmp[1].split(":")[1].replace('"',"")).replace(" ","")
		em = str(tmp[2].split(":")[1].replace('"',"")).replace(" ","")
	except:
		cr = "not present"
		em = "not present"
	print(cr)
	print(em)
work()
