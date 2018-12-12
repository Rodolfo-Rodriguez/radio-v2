#!/usr/bin/python2

import time

#time.tzset(-3)

time.altzone = -2

localtime = time.localtime()

year = localtime.tm_year
month = localtime.tm_mon
day = localtime.tm_mday

act_h = localtime.tm_hour
act_m = localtime.tm_min
act_s = localtime.tm_sec

# range [0, 6], Monday is 0
week_day = localtime.tm_wday

print localtime
print 'Date: ' + str(day) + '/' + str(month) + '/' + str(year) 
print 'Time: ' + str(act_h) + ':' + str(act_m) + ':' + str(act_s)
print 'Week Day: ' + str(week_day)

print 'Timezone: ' + str(time.altzone)