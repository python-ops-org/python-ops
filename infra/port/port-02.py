import csv
from datetime import datetime

def port():
#    try:
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log = open("%s.csv"%dt,"w+")
        writer=csv.writer(log)

        cmd='netstat -ntlp | grep 80'
        p=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, _=p.communicate()
        q=str(out)
        #print(q)
        pr = findall(':([^ ]+)', q)[0]
        print(pr)
        writer.writerow([pr])





    #except:
    #    print("na")

#port(80)
port()
