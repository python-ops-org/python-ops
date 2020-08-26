

import requests
import argparse
import json
import csv
from bs4 import BeautifulSoup
import re

#span class="ansi33"

token = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
headers = {"Content-Type": "application/json", "Authorization": "Bearer %s"%token}
#em = '123456'


def work():
	writing= open('output.csv', "w+")
	writer=csv.writer(writing)
	url = "http://192.168.56.159"
	next = "/api/v2/jobs/"
	print("job_id\turl\tcr\tem")
	writer.writerow(["job_id","url","cr","em"])
	while True:
		req = requests.get("%s%s"%(url,next),headers=headers)
		data = json.loads(req.text)
		ids = []
		for job in data["results"]:
			ids.append(job["id"])
#		print(ids)
		for id in ids:
			cr = "not available"
			#urls = ["/job_events/?search=war","/job_events/?search=jar","/job_events/?search=ear"]
			name = "not available"
			em = "123456"
			try:
				req_3 = requests.get("%s/api/v2/jobs/%s/"%(url,id),headers=headers)
				tmp_data = json.loads(req_3.text)
				val = json.loads(tmp_data["extra_vars"])
				try:
					name = val["war_url"]
				except:
					name  = "not available"
				cr = val["cr"]
#							em = tmp_data["extra_vars"].split("\n")[-1].split(" ")[1].replace('"',"")
				try:
					em = val["em"]
				except:
					pass
				print("%s\t%s\t%s\t%s"%(id,name,cr,em))
				writer.writerow([id,name,cr,em])
			except:
				print("%s\t%s\t%s\t%s"%(id,name,cr,em))
				writer.writerow([id,name,cr,em])
		if data["next"] == None:
			break
		else:
			next = data["next"]
	#quit()
	#print("here")
	writing.close()
	fo = open("output.csv","r")
	for line in fo:
		line = line.split(",")
		id = line[0]
		url = line[1]
		cr = line[2].replace("\n","")
		em = line[3]
		# is this the below patch commands necessary ?below part is correct...we had to only get cr from job url

		#is that job id static ?yes..
		if (".war" in url) or ("jar" in url) or (".ear" in url):
			if ("not available" not in cr):
						patch1 = {"name": "get_url_test_02","description": '',"job_type": "run","verbosity": cr, "nexus_url": url ,"em":em}
						tmp1 = requests.patch("http://192.168.56.159/api/v2/job_templates/17/",json=patch1,headers=headers)
						data_patch1 = json.loads(tmp1.text)
						ver = data_patch1["verbosity"]
						print(data_patch1)
						if tmp1.status_code == 200:
							patch2 = {"name": "get_url_test_03","description": '',"job_type": "run","verbosity": ver}
							tmp2 = requests.patch("http://192.168.56.159/api/v2/job_templates/18/",json=patch2,headers=headers)
							print(tmp2.text)
			else:
					continue
if __name__ == "__main__":
	work()
