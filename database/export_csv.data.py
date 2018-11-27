#!/usr/bin/python

import sys
sys.path.append('/home/pi/develop/radio-v2')

from app import db_manager

db_manager.export_csv_data()
