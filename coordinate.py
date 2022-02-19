###To mention calendar###################################################

import calendar
cal=calendar.month(2018,8)
print(cal)

###To mention time#######################################################

import datetime
now=datetime.datetime.now()
print(str(now))


###To mention desired time###############################################

print("%d" % now.day)
print("%d" % now.month)
print("%d" % now.year)
print("%d" % now.hour)
print("%d" % now.minute)
print("%d" % now.second)


### To mention desired time and date in single line#######################

print(now.strftime("%d-%m-%Y %H:%M"))

### To clear screen
import os
os.system('cls')

import urllib
funopen():
    return urllib.urlopen('https://www.youtube.com')

