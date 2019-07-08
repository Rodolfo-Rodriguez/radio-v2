
import os

from . import db
from . import CONFIG
from .models import Radios, Program, Artist, Playlist, Podcast, Artist_Link, Radio_Link, Podcast_Link, Bookmark, Preset, Episode

class DBManager():

  table_names = [
    'Radios',
    'Program',
    'Artist',
    'Playlist',
    'Podcast',
    'Radio_Link',
    'Artist_Link',
    'Podcast_Link',
    'Bookmark',
    'Preset',
    'Episode'
  ]

  def __init__(self,db):
    self.db = db

  def count_records(self,table_name):

    if table_name == 'Radios':
      return self.db.session.query(Radios).count()
    if table_name == 'Program':
      return self.db.session.query(Program).count()
    elif table_name == 'Artist':
      return self.db.session.query(Artist).count()
    elif table_name == 'Playlist':
      return self.db.session.query(Playlist).count()
    elif table_name == 'Podcast':
      return self.db.session.query(Podcast).count()
    elif table_name == 'Radio_Link':
      return self.db.session.query(Radio_Link).count()
    elif table_name == 'Artist_Link':
      return self.db.session.query(Artist_Link).count()
    elif table_name == 'Podcast_Link':
      return self.db.session.query(Podcast_Link).count()
    elif table_name == 'Bookmark':
      return self.db.session.query(Bookmark).count()
    elif table_name == 'Preset':
      return self.db.session.query(Preset).count()
    elif table_name == 'Episode':
      return self.db.session.query(Episode).count()

  def get_record_list(self, table_name):
      
    record_list = []

    if table_name == 'Radios':
      record_list = Radios.query.all()
    elif table_name == 'Program':
      record_list = Program.query.all()
    elif table_name == 'Artist':
      record_list = Artist.query.all()
    elif table_name == 'Playlist':
      record_list = Playlist.query.all()
    elif table_name == 'Podcast':
      record_list = Podcast.query.all()
    elif table_name == 'Radio_Link':
      record_list = Radio_Link.query.all()
    elif table_name == 'Artist_Link':
      record_list = Artist_Link.query.all()
    elif table_name == 'Podcast_Link':
      record_list = Podcast_Link.query.all()
    elif table_name == 'Bookmark':
      record_list = Bookmark.query.all()
    elif table_name == 'Preset':
      record_list = Preset.query.all()
    elif table_name == 'Episode':
      record_list = Episode.query.all()

    return record_list


  def create_record(self, table_name, id):
      
    if table_name == 'Radios':
      record = Radios(id=id)
    elif table_name == 'Program':
      record = Program(id=id)
    elif table_name == 'Artist':
      record = Artist(id=id)
    elif table_name == 'Playlist':
      record = Playlist(id=id)
    elif table_name == 'Podcast':
      record = Podcast(id=id)
    elif table_name == 'Radio_Link':
      record = Radio_Link(id=id)
    elif table_name == 'Artist_Link':
      record = Artist_Link(id=id)
    elif table_name == 'Podcast_Link':
      record = Podcast_Link(id=id)
    elif table_name == 'Bookmark':
      record = Bookmark(id=id)
    elif table_name == 'Preset':
      record = Preset(id=id)
    elif table_name == 'Episode':
      record = Episode(id=id)

    return record

  def csv_file(self, table_name):

    return os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, table_name.lower() + '.csv')

  def write_csv_file(self, table_name, record_list):

    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    for record in record_list:
      out_line = record.export_string()
      f.write(out_line)
    
    f.close()

    print "{} -> {} [{}]".format(table_name, csv_file, len(record_list))

  def read_csv_file(self, table_name):

    csv_file = self.csv_file(table_name)

    with open(csv_file,"r") as csv:
      
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        record = self.create_record(table_name, id)
        record.import_string(line)

        db.session.add(record)        
        db.session.commit()

      csv.close()

      record_count = self.count_records(table_name) 

      print "{} [{}]".format(table_name, record_count)


  ################################################################################################################################################################
  # Drop and Create Radio DB
  ################################################################################################################################################################

  def drop_and_create_db(self):

    self.db.drop_all()
    self.db.create_all()

  ################################################################################################################################################################
  # Export Data
  ################################################################################################################################################################

  def export_csv_data(self):

    print "===> Exporting Tables to Files"

    for table_name in self.table_names:
      record_list = self.get_record_list(table_name)
      self.write_csv_file(table_name, record_list)

  ################################################################################################################################################################
  # Import Data
  ################################################################################################################################################################

  def import_csv_data(self):

    print "===> Importing Tables from Files"

    for table_name in self.table_names:
      self.read_csv_file(table_name)
