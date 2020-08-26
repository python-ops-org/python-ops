import subprocess
from subprocess import Popen
from subprocess import Popen, PIPE


#subprocess.run executes a command and waits for it to finish
#
"""
 Popen you can continue doing your stuff while the process finishes and
 then just repeatedly call subprocess. communicate yourself
 to pass and receive data to your process
"""

"""
Note that, what subprocess.run is actually doing is invoking for
you the Popen and communicate, so you don't need to make a
loop to pass/receive data nor wait for the process to finish.

"""
def cmd():
    c = "free -m"
    """
    p = subprocess.run(c, stdout=subprocess.PIPE, shell=True)
    print(p)
    """
    p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=None, shell=True)
    o = p.communicate()
    print(o[0])


cmd()
