
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
		resp = ""
		for id in ids:
			urls = ["/job_events/?search=war","/job_events/?search=jar","/job_events/?search=ear"]
			name = ""
			for file_url in urls:
				req_2 = requests.get("%s/api/v2/jobs/%s%s"%(url,id,file_url),headers=headers)
				data_2 = json.loads(req_2.text)
				if len(data_2["results"]) == 8:
					refined = data_2["results"][6]["stdout"].split(",")
					for text in refined:
						if "url" in text:
							name = text.split('"url": "')[1].replace('"',"")
							patch = {"name": "Demo Job Template","description": "","job_type": "run","extra_vars": "nexus_url: %s"%name}
							tmp = requests.patch("http://192.168.56.159/api/v2/job_templates/7/",json=patch,headers=headers)
							#print(tmp.text)
							resp= tmp.text
							#print(tmp.status_code)
							#quit()
							break
					if name != "":
						print "%s\t%s"%(id,name)
						print(resp)
						writer.writerow([id,name])
						break
				else:
					#print "%s\tnot present"%id
					writer.writerow([id,"not present"])
					break
		if data["next"] == None:
			break
		else:
			next = data["next"]
work()
