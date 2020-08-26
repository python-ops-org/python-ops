import paramiko
import argparse
import pandas as pd


file = open("nodes.log", "a")
def log(message):
    print(message)
    file.write(message)

def para(ip, username, password, cmd, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port, username, password)
        _, stdout, _ = ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        log(f"{ip} {resp}")
    except:
        log(f"{ip} na")

def remote_info(info, command):
    for row in info:
        para(row["ip"], row["user"], row["pwd"], command)

def parse_csv(file_name):
    df = pd.read_csv(file_name)
    info = []
    for row in df.values:
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
    parser.add_argument("-i", dest="file", default="inv.csv", required=False, type=str, help="CSV file path")
    parser.add_argument("-c", dest="command", default="free -m", required=False, type=str, help="Command to execute remotely")
    args = parser.parse_args()

    info = parse_csv(args.file)
    remote_info(info, args.command)

if __name__ == '__main__':
    main()
