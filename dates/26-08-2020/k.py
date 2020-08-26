import subprocess
import csv
from datetime import datetime
import argparse


dt = datetime.now().strftime("%Y-%M-D_%H-%M-%s")
f1 = open("%s.csv"%dt, "a")
def log(message):
    print(message)
    f1.write(message)

#5/4



def parse_csv(filename):
    f2 = open(filename)
    reader = csv.reader(f2)
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



def remote(ip, user, pwd, cmd):
    c = f"sshpass -p {pwd}  -o StrictHostKeyChecking=No {user}@{ip} {cmd}"
    p = subprocess.run(c, stdout=subprocess.PIPE, shell=True)

    if p.stdout:
        log(f"{ip} {p.stdout.decode()}")
    else:
        log(f"{ip} na")

def remote_info(info, command):
    for row in info:
        remote(row["ip"],row["user"],row["pwd"], command)


def main():
    p = argparse.ArgumentParser():
    p.add_argument("-i", dest=file, required=false)
    p.add_argument("-c", dest=command, required=false)
    args = p.parse_args()

    info = parse_csv(args.file)
    remote_info(info, args.command)

if __name__ == '__main__':
    main()
