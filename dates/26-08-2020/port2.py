import re
import subprocess
from re import findall
import csv
from datetime import datetime

def port():
    try:
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log = open("%s.csv"%dt,"w+")
        writer=csv.writer(log)

        cmd='netstat -ntlp | grep 80'
        p=subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        q=p.stdout.decode("ascii")
        #print(q)
        pr = findall(':([^ ]+)', q)[0]
        #print(pr)
        #writer.writerow([pr])
        #if int(pr) == int(80):
        if int(pr) == None:
            print("notok")
        else:
            print("ok")
    except:
        print("notok")   

port()

