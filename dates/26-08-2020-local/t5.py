import subprocess,csv
from datetime import datetime

def cmd():
    c = 'free -m'
    p = subprocess.run(c, stdout=subprocess.PIPE, shell=True)
    data = str(p).split("        ")
    free = ""
    for val in data:
        if "Mem" in val:
            free=data[data.index(val)+2]
            break
    free = free.replace(" ","")
    dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log = open("%s.csv"%dt,"w+")
    writer=csv.writer(log)
    headers = ["free"]
    writer.writerow(headers)
    writer.writerow([free])
    log.close()
cmd()
#whats the data needed ?only free usage need to be written in csv
#t5 is not in same dir as 1py, open this directory to check csv output
#someone came..wait
