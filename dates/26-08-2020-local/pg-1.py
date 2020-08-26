from subprocess import Popen, PIPE
import argparse,shlex
import psycopg2

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
				conn = psycopg2.connect(host=row[0] ,port= row[1],dbname=row[4].replace("\n","") ,user=row[3] ,password=row[2])
				cursor = conn.cursor()
				cursor.execute(open(sql_name, "r").read())
				colnames = [desc[0] for desc in cursor.description]
				cols = ""
				for col in colnames:
					cols = cols+col+"\t"
				print(cols)
				data = cursor.fetchall()
				for j in range(len(data)):
					row = ""
					for i in range(len(colnames)):
						row = row+str(data[j][i]).replace(" ","")+"\t"
					print(row)
				cursor.close()
				conn.close()
#				print("success")
			except:
				print("failed to fetch")
parser = argparse.ArgumentParser()
parser.add_argument("-a")
parser.add_argument("-i")
parser.add_argument("-f")
args = parser.parse_args()
if (args.a == "connect") and (args.i is not None):
	check_db(args.i)
elif (args.a == "query") and (args.f is not None) and (args.i is not None):
	execute_db(args.i,args.f)
