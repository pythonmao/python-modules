import datetime

print datetime.datetime.now()
print datetime.datetime.today()
print datetime.datetime.utcnow()
print datetime.MAXYEAR
print datetime.MINYEAR

mm = datetime.timedelta(days=365)
mm1 = datetime.timedelta(days=364)
print mm
print abs(mm)
print mm-mm1
print mm.total_seconds()

from datetime import date

print date(2016, 8, 19)
print date.today()

import time

nn = time.time()
print nn
print date.fromtimestamp(nn)
#date2 = date1 + timedelta

print date(2002,12,4).timetuple() #time.localtime()
print date(2016,9,18).weekday()
print date(2016,9,18).isoweekday()
print date(2016,9,18).ctime()
# print date.__format__(format) #date.strftime()

# d = date.fromordinal(730920) # 730920th day after 1. 1. 0001

# d.strftime("%d/%m/%y")
import calendar

print calendar.monthrange(2016, 9)
print calendar.isleap(2016)
# print calendar.monthdayscalendar(2016,9)


