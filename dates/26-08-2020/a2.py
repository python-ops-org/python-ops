import subprocess
import datetime,csv

##need to fetch url with war from csv and execute with wget
#
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

    cmd = "wget %s"%url
    r = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

    if r.stdout:
        print(f"{r.stdout.decode()}")
    else:
        print(f"na")



if __name__ == '__main__':
    parse_csv()
