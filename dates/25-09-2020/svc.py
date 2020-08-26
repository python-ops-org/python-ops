def svc(serv):
    try:
        cmd='ps -ef | grep "%s"'%serv
        p=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, _=p.communicate()
        q=str(out)
        idx = q.split("      ")[1].split(" ")[0]
        idx = int(idx)
        print("'%s' service id: %s"%(serv,idx))
        #print(port_num)
    except:
        print("'%s' service id not found"%serv)

svc(sendmail)

