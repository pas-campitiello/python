import datetime, time

print("datetime.date                =", datetime.date)
print("datetime.time                =", datetime.time)
print()
print("datetime.date.today()        =", datetime.date.today())
print("datetime.date.today().year   =", datetime.date.today().year)
print("datetime.date.today().month  =", datetime.date.today().month)
print("datetime.date.today().day    =", datetime.date.today().day)
print()
print("datetime.datetime.now()                  =", datetime.datetime.now())
print("datetime.datetime.today()                =", datetime.datetime.today())
print("datetime.datetime.today().hour           =", datetime.datetime.today().hour)
print("datetime.datetime.today().minute         =", datetime.datetime.today().minute)
print("datetime.datetime.today().second         =", datetime.datetime.today().second)
print("datetime.datetime.today().microsecond    =", datetime.datetime.today().microsecond)
print("datetime.datetime.today().weekday()      =", datetime.datetime.today().weekday())
print("datetime.datetime.today().isoweekday()   =", datetime.datetime.today().isoweekday())
print("datetime.datetime.today().timetz()       =", datetime.datetime.today().timetz())
print()
print("time.ctime() =", time.ctime())
print()
timenow = datetime.datetime.now()
print("%Y-%m-%d_%H:%M:%S    =", timenow.strftime('%Y-%m-%d_%H:%M:%S'))
print("%D                   =", timenow.strftime('%D'))
print("%m-%d-%y             =", timenow.strftime('%m-%d-%y'))
print("%a %d/%m/%y          =", timenow.strftime('%a %d/%m/%y'))
print("%A %d/%m/%y          =", timenow.strftime('%A %d/%m/%y'))
print()
print("%A %b %d/%m/%y - %H:%M:%S    =", timenow.strftime('%A %b %d/%m/%y - %H:%M:%S'))
print("%a %B %d - %H:%M             =", timenow.strftime('%a %B %d - %H:%M'))
print("%d-%B-%Y                     =", timenow.strftime('%d-%B-%Y'))
print("%m-%d-%Y                     =", timenow.strftime('%m-%d-%Y'))
print("%d/%m/%Y                     =", timenow.strftime('%d/%m/%Y'))