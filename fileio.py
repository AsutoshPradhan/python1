import datetime;
import time;
day= str(datetime.datetime.now())

print (day)


f = open("log.txt", "a")

f.write(day)

f.write("\n")
f.close()


f=open("log.txt")
x=f.read()
print(x)
f.close()

