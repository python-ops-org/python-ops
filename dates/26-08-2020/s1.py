import subprocess
import argparse
import csv
import time
import sys


"""
def remote_info(info):
    for row in info:
        remote(row["ip"], row["user"], row["pwd"])
"""
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
        print(row_dict)
        info.append(row_dict)
    return info

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="file", default="inventory - Sheet1.csv", required=False, type=str, help="CSV file path")
    args = parser.parse_args()

    info = parse_csv(args.file)

if __name__ == '__main__':
    main()
