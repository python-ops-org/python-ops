from subprocess import Popen, PIPE
import argparse
import subprocess
import csv

def check_db(file_name):
    file = open("file_name", "a")
    lines = file.readlines()
    for row in lines[:1]:
        r1 = row.split(",")
        p = Popen('nc' , '-zv', '-w 5', row[0] , row[1], stdout=PIPE, stderr=PIPE )
        stdout, stderr = p.communicate()
        if 'succeeded' in p:
            print("%s %s connected  ."%(row[0],row[1]))
        else:
            print("%s %s connected ." %(row[0],row[1]))







p = argparse.ArgumentParser()
p.add_argument("-a")
p.add_argument("-i")
ar = p.parse_args()
if (ar.a == "connect")  and (ar.i is not None):
    check_db(ar.i)




    
