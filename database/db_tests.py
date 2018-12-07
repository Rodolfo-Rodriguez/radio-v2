#!/usr/bin/python

import sys, os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(base_path)


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models import Radios,Radio_Link

from sqlalchemy import create_engine
engine = create_engine("sqlite:///radio.db")

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

s = session()

radio_list = s.query(Radios).all()
nickname_list = []

for radio in radio_list:
	nickname_list.append(radio.nickname)


radio_link_list = s.query(Radio_Link).all()


################################################################################################################################################################
# Export Data
################################################################################################################################################################

radio_file = 'table_radio_v2.csv'

f = open(radio_file,"w")

for radio in radio_list:
	
	nickname = radio.nickname
	id = nickname_list.index(nickname) + 1

	out_line = str(id)
	out_line = out_line + "|" + str(radio.name)
	out_line = out_line + "|" + str(radio.url)
	out_line = out_line + "|" + str(radio.country)
	out_line = out_line + "|" + str(radio.num_plays)
	out_line = out_line + "|" + str(radio.style)
	out_line = out_line + "|" + str(radio.stars)
	out_line = out_line + "|" + str(radio.fav)
	out_line = out_line + "|" + str(radio.description)

	out_line = out_line.encode('utf-8')

	f.write(out_line + "\n")

f.close()


radio_link_file = 'table_radio_link_v2.csv'

f = open(radio_link_file,"w")

for radio_link in radio_link_list:
	
	nickname = radio_link.radio_nickname
	id = nickname_list.index(nickname) + 1
	
	out_line = str(radio_link.name)
	out_line = out_line + "|" + str(radio_link.url)
	out_line = out_line + "|" + str(id)

	out_line = out_line.encode('utf-8')

	f.write(out_line + "\n")

f.close()