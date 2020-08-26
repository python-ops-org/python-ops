import csv
import subprocess
import argparse
import sys
from subprocess import Popen, PIPE

file = open("nodes.log", "a")
def log(message):
    print(message)
    file.write(message)


def csv_parse(file_name):
    file = open(file_name)
    reader = csv.reader(file)
    next(reader)
    info = []

    for row in reader:
        row_dict = {
               "user": row[0],
               "pwd": row[1],
               "ip": row[2]
               }
        print(row_dict)
        info.append(row_dict)
    return info


def remote(ip, user, pwd, cmd):
    remote_cmd = f"sshpass -p {pwd} ssh -o StrictHostKeyChecking=no {user}@{ip} {cmd}"
    response = subprocess.run(remote_cmd, stdout=subprocess.PIPE, shell=True)
    if response.stdout:
        log(f"{ip} {response.stdout.decode()}")
    else:
        log(f"{ip} na")

def remote_info(info, command):
    for row in info:
        remote(row["ip"],row["user"],row["pwd"], command)




def main():
    p=argparse.ArgumentParser()
    p.add_argument("-i", required=False, dest="file")
    p.add_argument("-c", required=False, dest="command")
    a = p.parse_args()
    info = csv_parse(a.file)
    remote_info(info, a.command)

if __name__ == '__main__':
    main()
