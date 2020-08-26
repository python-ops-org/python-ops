import re import subprocess from re import findall

def port(portn):
    try:
        cmd='netstat -ntlp | grep "%s"'%portn
        p=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, _=p.communicate()
        q=str(out)
        port_num = findall(':([^ ]+)', q)[0]
        #print(port_num)
        if int(port_num) == int(portn):
            print("port no %s ok"%port_num)
       #     return(True)
        else:
            print("port no %s not ok"%port_num)
        #    return(False)
    except:
        print("port no %s not ok"%port_num)
        #return(False)
#this if is wrong, if what ???
port(3400) #use whatever port you want greped here










#    quit()
    
#    r6=re.findall(r'^[\w\d\s\.:]+:(25)\s+.*$',  str(out), re.MULTILINE | re.IGNORECASE)

#    print(r6)

#port()

"""
cmd ='tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      3400/sendmail: MTA:'
r7=re.findall(r'^[\w\d\s\.:]+:(25)\s+.*$',  cmd, re.MULTILINE)
print(r7[0])
"""
