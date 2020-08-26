import subprocess
import argparse
import csv
import os


def files():
    f=open("fi","r")
    a=f.readlines()
    for f2 in a:
        print(f2)
        create=subprocess.Popen(["touch", f2.replace("\n","")], stdout=subprocess.PIPE)
files()        


"""
def files():
    f=open("fi","r")
    for f2 in f:
        print(f2)
        f2 = f2.replace("\n","")
        tmp = open(f2,"w+")
        tmp.close()
files()
"""



























