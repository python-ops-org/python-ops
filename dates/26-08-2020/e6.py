import argparse
import subprocess
import os
import csv


f2 = open("nodes.log", "a")
def log(message):
    print(message)
    f2.write(message)


def connect_db(csv_file):
    file = open("csv_file")
    reader = file.readlines()
    for row in reader[1:]:
        row = row.split(",")
        p   = Popen(['nc', '-zv', '-w 5', row[0],row[1]], stdout=PIPE, stderr=PIPE)
        if "succeeded in stdout":
            log("%s %s connected ."%(row[0],row[1]))
        else:
            log("%s %s not connected. "%(row[0],row[1])

def db_query(csv_file,sql_file):
     file = open("csv_file")
     reader = file.readlines()
     for row in reader[1:]:
             try:
                     row = row.split(",")
                     p = 'PGPASSWORD=%s psql -h %s -p %s -u %s -d %s -f "%s"'%(row[2],row[0],row[1],row[3],row[4],sql_file)
                     os.system(p.replace("\n", ""))
             except:
                     print("NA")

p = argparse.ArgumentParser()
p.add_argument("-i")
p.add_argument("-f")
p.add_argument("-a")
args=p.parse_args()
if (args.a == connect) and (args.i is not None)
    connect_db(args.i)
elif(args.a == query) and (args.i is not None) and (args.f is not None)
    db_query(args.i,args.f)
