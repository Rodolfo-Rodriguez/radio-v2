#!/usr/bin/python2

import os
base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:////home/pi/develop/radio-v3/database/radio2.db', echo=True)

conn = engine.connect()

stmt = text("SELECT count(*) FROM Radios")

result = conn.execute(stmt)

print result
