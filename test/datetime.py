#!/usr/bin/python2

import datetime
	
## Format Today
#today = datetime.date.today()
#today = datetime.datetime.utcnow()
#today_txt = today.strftime("%a, %d %b de %Y %H:%M:%S")


#	HERE = tz.tzlocal()
now = datetime.datetime.now()

today_txt = now.strftime("%a, %d %b de %Y %H:%M:%S")
print today_txt


