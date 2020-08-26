import subprocess
import argparse
import csv
import time
import sys


file = open("nodes.log", "a")
def log(message):
    print(message)
    file.write(message)

def remote(ip, usr, pwd, cmd):
    remote_cmd = f"sshpass -p {pwd} ssh -o StrictHostKeyChecking=no {usr}@{ip} {cmd}"
    response = subprocess.run(remote_cmd, stdout=subprocess.PIPE, shell=True)
    
    if response.stdout:
        log(f"{ip} {response.stdout.decode()}")
    else:
        log(f"{ip} na")

def remote_info(info, command):
    for row in info:
        remote(row["ip"], row["user"], row["pwd"], command)

def parse_csv(file_name):
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
        info.append(row_dict)
    return info

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="file", default="inventory - Sheet1.csv", required=False, type=str, help="CSV file path")
    parser.add_argument("-c", dest="command", default="free -m", required=False, type=str, help="Command to execute remotely")
    args = parser.parse_args()

    info = parse_csv(args.file)
    remote_info(info, args.command)

if __name__ == '__main__':
    main()
