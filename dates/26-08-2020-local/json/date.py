import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 3)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday)
print(tomorrow)


fdate = datetime.datetime.strptime(fdate, '%Y/%m/%d').strftime('%d%m%y')
print datetime.date.today()

from datetime import date, datetime
fdate = datetime.strptime(fdate, '%Y/%m/%d').strftime('%d%m%y')
print date.today()


import arrow 
  
utc_time = arrow.utcnow() 
print(utc_time) 


import subprocess
import os

###yesterday

yesterday='date -d "$date -2 days" +"%Y-%m-%d"'
t1 = subprocess.run(yesterday, stdout=subprocess.PIPE, shell=True)
t2=t1.stdout.rstrip()
t3=str(t2,'utf-8')
print(t3)


####today

today='date +"%Y-%m-%d"'

t5 = subprocess.run(today, stdout=subprocess.PIPE, shell=True)
t6=t5.stdout.rstrip()
t7=str(t6,'utf-8')
print(t7)
