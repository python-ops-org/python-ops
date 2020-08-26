import subprocess
from datetime import datetime


def cmd():
    c = 'free -m'
    p = subprocess.run(c, stdout=subprocess.PIPE, shell=True)
    print(str(p))
    dt = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    log = open("%s.log"%dt,"w+")
    log.write(str(p))
    log.close()
cmd()
