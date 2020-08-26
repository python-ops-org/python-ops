import argparse,shlex
import psycopg2
import os 
from subprocess import Popen, PIPE
def check_db(csv_name):
	with open(csv_name,"r") as ff:
		lines = ff.readlines()
		for row in lines[1:]:
			row = row.split(",")
			process = Popen(['nc', '-zv', '-w 5',row[0],row[1]], stdout=PIPE, stderr=PIPE)
			stdout, stderr = process.communicate()
			if "succeeded" in stdout:
				print("%s %s connected ."%(row[0],row[1]))
			else:
				print("%s %s failed."%(row[0],row[1]))
def execute_db(csv_name,sql_name):
	with open(csv_name,"r") as ff:
		lines = ff.readlines()
		for row in lines[1:]:
			try:
				row=row.split(",")
				cmd = 'PGPASSWORD=%s psql -h %s -p %s -U %s -d %s -f "%s"'%(row[2],row[0],row[1],row[3],row[4],sql_name)
				os.system(cmd.replace("\n",""))
			except:
				print("NA")
parser = argparse.ArgumentParser()
parser.add_argument("-a")
parser.add_argument("-i")
parser.add_argument("-f")
args = parser.parse_args()
if (args.a == "connect") and (args.i is not None):
	check_db(args.i)
elif (args.a == "query") and (args.f is not None) and (args.i is not None):
	execute_db(args.i,args.f)

