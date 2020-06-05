import requests
import argparse
import json
import csv
from bs4 import BeautifulSoup
import re

#span class="ansi33"

token = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
headers = {"Content-Type": "application/json", "Authorization": "Bearer %s"%token}



def war_hit(file_name):
	fo = open(file_name,"r")
	for line in fo:
		url_from_csv = line.split(",")[1]
		if (".war" in url_from_csv) or ("jar" in url_from_csv) or (".ear" in url_from_csv):	
			patch = {"name": "Demo Job Template","description": "","job_type": "run","extra_vars": "nexus_url: %s"%url_from_csv}
			req = requests.patch("http://192.168.56.159/api/v2/job_templates/7/",json=patch,headers=headers)
			if req.status_code == 200:
				print req.text 





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
			urls = ["/job_events/?search=war","/job_events/?search=jar","/job_events/?search=ear"]
			url_grabbed = ""
			for file_url in urls:
				req_2 = requests.get("%s/api/v2/jobs/%s%s"%(url,id,file_url),headers=headers)
				data_2 = json.loads(req_2.text,strict=False)
				for trial in data_2["results"]:
					try:
						url_grabbed = trial["event_data"]["res"]["url"]
						if (".war" in url_grabbed) or ("jar" in url_grabbed) or (".ear" in url_grabbed):
							url_grabbed = trial["event_data"]["res"]["url"]
						else:
							url_grabbed = ""
					except:
						continue
			if name != "":
				print "%s\t%s"%(id,url_grabbed)
				writer.writerow([id,url_grabbed])
			else:
				print "%s\tnot present"%id
				writer.writerow([id,"not present"])
		if data["next"] == None:
			break
		else:
			next = data["next"]

	war_hit("output.csv")
if __name__ == '__main__':
	work()
