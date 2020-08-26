import glob,subprocess
import os.path
from os import path
fmrs = glob.glob("/home/nik/Desktop/python-ops/study/new-01/t1/*.FMR")
if path.exists("/home/nik/Desktop/python-ops/study/new-01/t2/"):
    pass
else:
    create=subprocess.call("mkdir -p t2",shell=True)
i = 0
for fmr in list(fmrs):
    f_id = i
    if i < 10:
        f_id = "0%s"%i
    new_name=""
    tmp = fmr.split("/")
    fmr_name = tmp[len(tmp)-1]
    sliced = fmr_name.split("_")
    for q in sliced:
        if sliced.index(q) == 3:
            new_name=new_name+"_"+f_id
        else:
            new_name=new_name+"_"+q
    print(new_name[1:])
    copy=subprocess.call("cp %s /home/nik/Desktop/python-ops/study/new-01/t2/%s"%(fmr,new_name[1:]),shell=True)
    i=i+1


