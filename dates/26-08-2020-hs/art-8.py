
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
	writing= open('output.csv', "w+")
	writer=csv.writer(writing)
	url = "http://192.168.56.159"
	next = "/api/v2/jobs/"
	print "job_id\turl"
	writer.writerow(["job_id","url"])
        ids = [42]
#	while True:
	for id in ids:
			urls = ["/job_events/?search=war","/job_events/?search=jar","/job_events/?search=ear"]
			name = ""
			for file_url in urls:
				req_2 = requests.get("%s/api/v2/jobs/%s%s"%(url,id,file_url),headers=headers)
				data_2 = json.loads(req_2.text,strict=False)
				for trial in data_2["results"]:
					try:
						name = trial["event_data"]["res"]["url"]
					except:
						continue
			if name != "":
				print "%s\t%s"%(id,name)
				writer.writerow([id,name])
				break
			else:
				print "%s\tnot present"%id
				writer.writerow([id,"not present"])
				break
work()
