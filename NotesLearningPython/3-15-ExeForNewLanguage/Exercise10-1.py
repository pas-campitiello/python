import datetime

timenow = datetime.datetime.now()
timestamp = timenow.strftime('%Y%m%d%H%M')
print(timestamp)

name = ()

f = open("contentfile-" + timestamp + ".txt", "w")
contents = f.write("Content in the new file with this timestamp " + timestamp)
f.close()T
