import re
import json
from datetime import datetime as dt
import subprocess
import argparse
import csv
import pandas as pd


def play(fur,sur):
    cmd2 = "ansible-playbook -i %s %s"%(fur,sur)
    p = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)  
    out, err = p.communicate()
    print(out)
    #return out

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-i")
	parser.add_argument("-f")
	args = parser.parse_args()
	if (args.i is not None) and (args.f is not None):
		play(args.i,args.f)
	else:
		print("Missing arguments")
