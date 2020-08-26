import re
import subprocess
from re import findall

def port(portn):
    try:
        cmd='netstat -ntlp | grep "%s"'%portn
        p=subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        
        q=str(p)
        port_num = findall(':([^ ]+)', q)[0]
        print(port_num)
        
        quit()
        if int(port_num) == int(portn):
            print("port no %s ok"%port_num)
       #     return(True)
        else:
            print("port no %s not ok"%port_num)
        #    return(False)
    except:
        print("port no %s not ok"%port_num)
        #return(False)

port(25)












cmd ='tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      3400/sendmail: MTA:'
#r7=re.findall(r'^[\w\d\s\.:]+:(25)\s+.*$',  cmd, re.MULTILINE)
r7 = findall(':([^ ]+)', cmd)
print(r7)

