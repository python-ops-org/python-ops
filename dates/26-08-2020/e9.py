import subprocess
import csv
import os


f2 = open("nodes.log", "a")
def log(message):
    print(message)
    f2.write(message)



def csv_parse(file_name):
    file = open("file_name")
    reader = csv.reader(file)
    next(reader)
    info = []
    for row in reader:
        row_dict = {
             "user": row[0],
             "pwd": row[1],
             "ip": row[2]
             }

        info.append(row_dict)
    return info

def remote(user,pwd,ip,cmd):
    c = f"sshpass -p {pwd} ssh -o StrictHostKeyChecking=no {user}@{ip} {cmd}"
    p = subprocess.run(c, stdout=subrpcess.PIPE, shell=True)
    if response.stdout:
        log(f"{ip}" "{response.stdout.decode()}")
    else:
        log(f"{ip}" na)

def remote_info(info, command):
    for row in info:
        remote(row["ip"],row["user"],row["ip"], command)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-i",dest="file",required=False)
    p.add_argument("-c",dest="command",required=False)
    args = p.parse_args()

    info = csv_parse(args.file)
    remote_info(info,args.command)


    if __name__ == '__main__':
        main()
