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
