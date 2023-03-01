import datetime

time_now=datetime.datetime.now()

yesterday=time_now.day-1
tomorrow=time_now.day+1
uakyt1=datetime.datetime(time_now.year, time_now.month, yesterday)
uakyt2=datetime.datetime(time_now.year, time_now.month, tomorrow)
print(time_now)
print(uakyt1)
print(uakyt2)