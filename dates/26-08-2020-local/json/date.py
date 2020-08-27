import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 3)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday)
print(tomorrow)
