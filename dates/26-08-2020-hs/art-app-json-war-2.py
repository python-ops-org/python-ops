
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
	urls = ["/job_events/?search=war","/job_events/?search=jar","/job_events/?search=ear"]
	name = ""
	fo = open("/home/nik/Desktop/python-ops/study/new-01/ap.json","r")
	data_2 = json.load(fo,strict=False)
	for trial in data_2["results"]:
		try:
			print trial["event_data"]["res"]["url"]
		except:
			continue
work()
