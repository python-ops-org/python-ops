import subprocess
import datetime,csv
import requests

dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log = open("%s.csv"%dt,"w+")
writer=csv.writer(log)

def parse_csv():
    with open("link.csv","r") as file:
        reader = csv.reader(file)
        links = []
        for row in reader:
            if ".war" in row[1]:
                links.append(row[1])
        for curr_link in links:
            foo(curr_link)

def foo(url):
    user = ""
    password = ""
    headers={"user":user,"password":password}
    r = requests.get(url,headers=headers)
    print(r.text)



#use os you cant, os wont store the output
#just inject the request module syntx...i will try here

if __name__ == '__main__':
    parse_csv()
