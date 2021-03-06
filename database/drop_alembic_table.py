#!/usr/bin/python

import sys
sys.path.append('/home/pi/develop/radio-v3')

from sqlalchemy import inspect
from app import db

inspector = inspect(db.engine)

table_names = inspector.get_table_names()

if 'alembic_version' in table_names:
        db.engine.execute('DROP TABLE alembic_version')


print "==========================="
print "Tables"
print "==========================="

for table in table_names:
        print table
