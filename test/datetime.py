#!/usr/bin/python2

import datetime

d = datetime.date(2008, 12, 22)

print d

month_name = 'Dec'
month_number = datetime.datetime.strptime(month_name, '%b').month

print month_number