import datetime
import requests
import sys

current_time = datetime.datetime.now()
current_time_string = current_time.strftime("%d-%b-%Y-%H-%M")

arg = sys.argv[1]

def runhttp(arg):
    st = ''
    st+=arg+'\n'
    for k in range(3):
        try:
            r = requests.head(arg)
            status = r.status_code
            status = str(status)
            print status
            st +=status+'\n'
        except:
            pass

    f2 = open('status'+current_time_string+'.txt', 'a')
    f2.write(st)
    f2.close()
    
def runfile(arg):
    f1 = open(arg, 'r')

    a = f1.readlines()
    urls = [url.strip() for url in a ]
    urls.remove('')

    for i in urls:
        print i
        st = ''
        st+=i+'\n'
        for k in range(3):
            try:
                r = requests.head(i)
                status = r.status_code
                status = str(status)
                print status
                st +=status+'\n'
            except:
                pass

        f2 = open('status'+current_time_string+'.txt', 'a')
        f2.write(st)
        f2.close()

    f1.close()

if 'http' in arg:
    runhttp(arg)
else:
    runfile(arg)




