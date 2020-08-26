#q=0

"""
def lockdown():
    stayhome()
    return
    goout()
    meetfriends()
    playsport()
    diningout()
    #hangoutwithgirlfriend

while q:
  lockdown()

"""
"""
def lockdown(locked):
  print("qurantined " + locked)

lockdown("stayhome")
lockdown("no meetingwithfriends")
lockdown("no sport")
lockdown("no pub")
lockdown("no alcohol")
lockdown("no hangoutwithgirlfriend")

"""
"""
CRED = '\033[91m'
CEND = '\033[0m'

list = ["stay home", "no sport", "no beer", "no hangout with gf"]

i = 0
while i < len(list):
    e = list[i]
    i += 1
    print(e)
else:
    print(CRED + "QURANTINED!" + CEND)
"""


"""
class Colors:
    RED = "\033[0;31m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
print(Colors.UNDERLINE  + "Quora" + Colors.END)
"""


def lockdown(item):
  print("\033[91m\033[4mLOCKDOWN:\033[0m")  
  for x in item:
    print(x)
  else:
    print("\033[91mHAPPY QURANTINED!\033[0m")  

list = ["stay home", "no sport", "no beer", "no hangout with gf"]
lockdown(list)


















