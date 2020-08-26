import json
import argparse


def meta(date):
        name = ""
        fo = open("metadata.json","r")
        data_2 = json.load(fo,strict=False)
        print("Timestamp\tID\tSelf Link\tSource Disk\tSource Disk Id")
        for elem in data_2:
            if date in elem["creationTimestamp"]:
                 ts = elem["creationTimestamp"]
                 id = elem["id"]
                 self_link = elem["selfLink"]
                 dsk = elem["sourceDisk"]
                 dsk_id = elem["sourceDiskId"]
                 print("%s\t%s\t%s\t%s\%s"%(ts,id,self_link,dsk,dsk_id))
        quit()

def meta_(date,param):
        name = ""
        fo = open("metadata.json","r")
        data_2 = json.load(fo,strict=False)
        print("Timestamp\t%s"%param)
        for elem in data_2:
            if date in elem["creationTimestamp"]:
                  ts = elem["creationTimestamp"]
                  val = elem[param]
                  print("%s\t%s"%(ts,val))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d")
    parser.add_argument("-p")
    args = parser.parse_args()
    if (args.d is not None) and (args.p is None):
        meta(args.d)
    if (args.d is not None) and (args.p is not None):
        meta_(args.d,args.p)
    else:
        print("kindly parse correct key")
        return None

if __name__ == "__main__":
    main()         







