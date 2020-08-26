import paramiko
import csv
import argparse

f = open("nodes.log", "a")
def log(message):
    print(message)
    f.write(message)
#-1 written log instead of message

def csv_parse(file_name):
    f = open("file_name")
    r = csv.reader(f)
    next(r)
    info = []
    for row in r:
        row_dict = {
            "user": row[0],
            "pwd":  row[1],
            "ip":   row[2]
        }
        info.append(row_dict)
        return info
#-3 did nt provide info = [], info.append(row_dict),return info

def remote(ip,user,pwd,cmd):
    ssh = paramiko.sshclient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #set = sun missing host = holand key = kitchen policy = poland
    try:
        ssh.connect(ip,port,username,password):
        _,stdout, = ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        log(f"{ip} {resp})
    except:
        log(f"{ip} na")        











def remote_info(info, command):
    for row in info:
        remote(row["ip"],row["user"],row["pwd"], command)

#5/5 good



def main():
    p = argparse.ArgumentParser()
    p.add_argument("-i", dest="file",required=False)
    p.add_argument("-c", dest="file", required=False)
    args = p.parse_args()

    info = csv.parse(args.filename)
    remote_info(info, args.command)

# -4 written parseargs instead of parse_args,written argument_add instead of add_argument
# written c instead of info, did nt provide remote_info functiom..could nt put info and args.command inside of it


if __name__ = '__main__':
    main()
