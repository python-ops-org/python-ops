import csv
import json,socket
import requests
import re
from datetime import datetime
from requests.auth import HTTPBasicAuth



def mail(report):
         msg = MIMEMultipart()
	 msg["From"] = "me@example.com"
	 msg["To"] = "sudipta1436@gmail.com"
	 msg["Subject"] = "Report Ansible."
         part = MIMEBase('application', "octet-stream")
       	 part.set_payload(open(report, "rb").read())
	 Encoders.encode_base64(part)
         part.add_header('Content-Disposition', 'attachment', filename=report)
         msg.attach(part)
         p =subprocess.Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=subprocess.PIPE)
	 p.communicate(msg.as_string())




def hosts():
    ips=[]
    page=1
    while True:
        try:
            url = 'http://localhost/api/v2/hosts?page=%s&page_size=100'%page
            r = requests.get(url, auth=HTTPBasicAuth('admin', 'password'))
            data = json.loads(r.text)
            num = len(data["results"])
	    if data["next"] == "null":
	        	for i in range(0,num):
				ip=data["results"][i]["name"]
		        	ips.append(ip)
		        	return ips
	    else:
			for i in range(0,num):
	   	    		ip=data["results"][i]["name"]
		        	ips.append(ip)
		        page=page+1
	except Exception as e:
	           return ips
hosts= hosts()
current_time=datetime.now()
date_format=current_time.strftime("%Y-%m-%d-%H-%M-%S")
namefile="%s.csv" %(date_format)
with open(namefile, "a") as fl:
	opt=csv.writer(fl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	opt.writerow(["IP"])
	for row in hosts:
    		print row
		opt.writerow([row])

