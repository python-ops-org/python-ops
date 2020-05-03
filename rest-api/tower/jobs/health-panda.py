import re
import json
from datetime import datetime as dt
import subprocess
import argparse
import csv
import pandas as pd


def play(fur,sur):
    cmd2 = "ansible-playbook -i %s %s"%(fur,sur)
    p = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)  
    out, err = p.communicate()
    outs = out.decode().split("\n")
    #print(outs)
    #quit()
    hosts = []
    nodes = []
    dists = []
    cpus = []
    mems = []
    for line in outs:
        if "ansible_default_ipv4.address" in line:
            hosts.append(line.split(":")[1].replace(" ","").replace('"',""))
        if "ansible_nodename" in line:
            nodes.append(line.split(":")[1].replace(" ","").replace('"',""))
        if "Print dist" in line:
            j=0
            while True:
                try:
                    pl = outs[outs.index(line)+2+j]
                    dists.append(pl.split(":")[1].replace(" ","").replace('"',""))
                    j=j+3
                except:
                    break
        if "Print cpu" in line:
            j=0
            while True:
                try:
                    pl = outs[outs.index(line)+2+j]
                    cpus.append(pl.split(":")[1].replace(" ","").replace('"',""))
                    j=j+3
                except:
                    break
        if "Print mem" in line:
            j=0
            while True:
                try:
                    pl = outs[outs.index(line)+2+j]
                    mems.append(pl.split(":")[1].replace(" ","").replace('"',""))
                    j=j+3
                except:
                    break
    #print(hosts)
    #print(nodes)
    #print(dists)
    #print(cpus)
    #print(mems)
    out_data = []
    print("IP\tNODENAME\tDIST\tCPU\tMEMORY")
    for i in range(len(hosts)):
        print("%s\t%s\t%s\t%s\t%s"%(hosts[i],nodes[i],dists[i],cpus[i],mems[i]))
        out_data.append([hosts[i],nodes[i],dists[i],cpus[i],mems[i]])
    #print(out_data)
    writer = pd.DataFrame(out_data,columns=["IP","NODENAME","DIST","CPU","MEMORY"])
    writer.to_csv("/home/nik/Desktop/report/%s.csv"%dt.now(),index=False)
    #return out

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-i")
	parser.add_argument("-f")
	args = parser.parse_args()
	if (args.i is not None) and (args.f is not None):
		play(args.i,args.f)
	else:
		print("Missing arguments")
