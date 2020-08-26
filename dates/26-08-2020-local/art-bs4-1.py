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
	while True:
		req = requests.get("%s%s"%(url,next),headers=headers)
		data = json.loads(req.text)
		ids = []
		for job in data["results"]:
			ids.append(job["id"])
		for id in ids:
			req_2 = requests.get("%s/api/v2/jobs/%s/stdout/"%(url,id),headers=headers)
			soup = BeautifulSoup(req_2.content,"html.parser")
			all_spans = soup.findAll("span",{"class":"ansi33"})
			name = ""
			for span in all_spans:
				if ((".war" in span.text) or (".jar" in span.text)) and ("url" in span.text):
					name = span.text.split('"url": ')[1][1:-1]
			if name == "":
				print "%s\tnot present"%id
				writer.writerow([id,"not present"])
			else:
				print "%s\t%s"%(id,name)
				writer.writerow([id,name])
		if data["next"] == None:
			break
		else:
			next = data["next"]
work()
