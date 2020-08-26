import paramiko
import argparse
import csv
#import panda

ip='192.168.56.162'
port=22
username=''
password=''

#cmd='ls /opt/apps'
cmd='free -m'
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
"""
stdin,stdout,stderr=ssh.exec_command('free -m')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
"""
