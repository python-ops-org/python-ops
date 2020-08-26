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
	print("job_id\turl\tcr")
	writer.writerow(["job_id","url","cr"])
	while True:
		req = requests.get("%s%s"%(url,next),headers=headers)
		data = json.loads(req.text)
		ids = []
		for job in data["results"]:
			ids.append(job["id"])
		for id in ids:
			cr = "not available"
			urls = ["/job_events/?search=war","/job_events/?search=jar","/job_events/?search=ear"]
			name = "not available"
			for file_url in urls:
				req_2 = requests.get("%s/api/v2/jobs/%s%s"%(url,id,file_url),headers=headers)
				data_2 = json.loads(req_2.text,strict=False)
				for trial in data_2["results"]:
					try:
						name = trial["event_data"]["res"]["url"]
					except:
						continue
			if name != "":
				req_3 = requests.get("%s/api/v2/jobs/%s/"%(url,template),headers=headers)
				tmp_data = json.loads(req_3.text)
				#try:
				val = json.loads(tmp_data["extra_vars"])
				cr = val["cr"] #y u have kept it in "" its json bro
				#except exception as e:
				#	pass
				print("%s\t%s\t%s"%(id,name,cr))
				writer.writerow([id,name,cr])
			else:
				print("%s\t%s\t%s"%(id,name,cr))
				writer.writerow([id,name,cr])
		if data["next"] == None:
			break
		else:
			next = data["next"]
	writing.close()
	fo = open("output.csv","r")
	for line in fo:
		line = line.split(",")
		id = line[0]
		url = line[1]
		cr = line[2].replace("\n","")
		if (".war" in url) or ("jar" in url) or (".ear" in url):
			if ("not available" not in cr):
						patch1 = {"name": "get_url_test_02","description": '',"job_type": "run","verbosity": cr,"nexus_url": url}
						tmp1 = requests.patch("http://192.168.56.159/api/v2/job_templates/17/",json=patch1,headers=headers)
						data_patch1 = json.loads(tmp1.text)
						ver = data_patch1["verbosity"]
						if tmp1.status_code == 200:
							patch2 = {"name": "get_url_test_03","description": '',"job_type": "run","verbosity": ver,}
							tmp2 = requests.patch("http://192.168.56.159/api/v2/job_templates/18/",json=patch2,headers=headers)
							print(tmp2.text)
			else:
					continue
work()
