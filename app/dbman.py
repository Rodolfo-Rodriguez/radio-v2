
import os

from . import db
from . import CONFIG
from .models import Radios, Program, Artist, Playlist, Podcast, Artist_Link, Radio_Link, Podcast_Link

class DBManager():

  db

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


  ################################################################################################################################################################
  # Drop and Create Radio DB
  ################################################################################################################################################################

  def drop_and_create_db(self):

    self.db.drop_all()
    self.db.create_all()


  ################################################################################################################################################################
  # Import Data
  ################################################################################################################################################################

  def import_csv_data(self):

  # ----------------------------------- Radios ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_RADIOS_TABLE_FILE)

    with open(csv_file,"r") as csv:

      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        url = words[2].decode('utf-8')
        image = words[3].decode('utf-8')
        country = words[4].decode('utf-8')
        num_plays = int(words[5])
        style = words[6].decode('utf-8')
        stars = int(words[7])
        fav_txt = words[8]
        if fav_txt == 'True':
          fav = True
        else:
          fav = False
        description = words[9].decode('utf-8')

        record = Radios(id=id,
                        name=name,
                        url=url,
                        image=image,
                        country=country,
                        num_plays=num_plays,
                        style=style,
                        stars=stars,
                        fav=fav,
                        description=description)

        db.session.add(record)
        db.session.commit()

    csv.close()

# ----------------------------------- Program ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PROGRAM_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        times = words[2].decode('utf-8')
        week_days = words[3].decode('utf-8')
        description = words[4].decode('utf-8')
        style = words[5].decode('utf-8')
        stars = int(words[6])
        fav_txt = words[7].decode('utf-8')
        if fav_txt == 'True':
          fav = True
        else:
          fav = False
        twitter = words[8].decode('utf-8')
        radio_id = int(words[9])

        radio = Radios.query.filter_by(id=radio_id).first()

        record = Program(id=id,
                        name=name,
                        times=times,
                        week_days=week_days,
                        description=description,
                        style=style,
                        stars=stars,
                        fav=fav,
                        twitter=twitter,
                        radios=radio)

        db.session.add(record)
        db.session.commit()

    csv.close()

# ----------------------------------- Artist ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_ARTIST_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        image = words[2].decode('utf-8')
        country = words[3].decode('utf-8')
        description = words[4].decode('utf-8')
        style = words[5].decode('utf-8')
        stars = words[6]
        fav = words[7]

        record = Artist(id=id,
                        name=name,
                        image=image,
                        country=country,
                        description=description,
                        style=style,
                        stars=stars)

        db.session.add(record)
        db.session.commit()

    csv.close()

  # ----------------------------------- Playlist ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PLAYLIST_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        image = words[2].decode('utf-8')
        playlist = words[3].decode('utf-8')
        description = words[4].decode('utf-8')
        type = words[5].decode('utf-8')

        record = Playlist(id=id,
                          name=name,
                          image=image,
                          playlist=playlist,
                          description=description,
                          type=type)

        db.session.add(record)
        db.session.commit()

    csv.close()

  
  # ----------------------------------- Podcast ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PODCAST_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        image = words[2].decode('utf-8')
        playlist = words[3].decode('utf-8')
        country = words[4].decode('utf-8')
        description = words[5].decode('utf-8')
        style = words[6].decode('utf-8')
        stars = int(words[7])
        feed_url = words[8].decode('utf-8')
        feed_filter = words[9].decode('utf-8')
        pod_dir = words[10].decode('utf-8')
        publisher = words[11].decode('utf-8')
        priority = int(words[12])

        fav_txt = words[13]
        if fav_txt == 'True':
          fav = True
        else:
          fav = False

        retag_txt = words[14]
        if retag_txt == 'True':
          retag = True
        else:
          retag = False


        record = Podcast(id=id,
                        name=name,
                        image=image,
                        playlist=playlist,
                        country=country,
                        description=description,
                        style=style,
                        stars=stars,
                        feed_url=feed_url,
                        feed_filter=feed_filter,
                        pod_dir=pod_dir,
                        publisher=publisher,
                        priority=priority,
                        fav=fav,
                        retag=retag)

        db.session.add(record)
        db.session.commit()

    csv.close()

  # ----------------------------------- Radio Links ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_RADIO_LINK_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        url = words[2].decode('utf-8')
        radio_id = int(words[3])

        radio = Radios.query.filter_by(id=radio_id).first()

        record = Radio_Link(id=id,
                            name=name,
                            url=url,
                            radios=radio)

        db.session.add(record)
        db.session.commit()

    csv.close()


# ----------------------------------- Artist Links ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_ARTIST_LINK_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        
        id = int(words[0])
        name = words[1].decode('utf-8')
        url = words[2].decode('utf-8')
        artist_id = int(words[3])

        artist = Artist.query.filter_by(id=artist_id).first()

        record = Artist_Link(id=id,
                              name=name,
                              url=url,
                              artist=artist)

        db.session.add(record)
        db.session.commit()

    csv.close()


  # ----------------------------------- Podcast Links ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PODCAST_LINK_TABLE_FILE)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        url = words[2].decode('utf-8')
        podcast_id = int(words[3])

        podcast = Podcast.query.filter_by(id=podcast_id).first()

        record = Podcast_Link(id=id,
                              name=name,
                              url=url,
                              podcast=podcast)

        db.session.add(record)
        db.session.commit()

    csv.close()


  ################################################################################################################################################################
  # Export Data
  ################################################################################################################################################################

  def export_csv_data(self):

   # ----------------------------------- Radio ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_RADIOS_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Radios.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.url)
      out_line = out_line + "|" + str(record.image)
      out_line = out_line + "|" + str(record.country)
      out_line = out_line + "|" + str(record.num_plays)
      out_line = out_line + "|" + str(record.style)
      out_line = out_line + "|" + str(record.stars)
      out_line = out_line + "|" + str(record.fav)
      out_line = out_line + "|" + str(record.description)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()

  # ----------------------------------- Program ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PROGRAM_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Program.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.times)
      out_line = out_line + "|" + str(record.week_days)
      out_line = out_line + "|" + str(record.description)
      out_line = out_line + "|" + str(record.style)
      out_line = out_line + "|" + str(record.stars)
      out_line = out_line + "|" + str(record.fav)
      out_line = out_line + "|" + str(record.twitter)
      out_line = out_line + "|" + str(record.radio_id)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()

  # ----------------------------------- Playlist ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PLAYLIST_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Playlist.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.image)
      out_line = out_line + "|" + str(record.playlist)
      out_line = out_line + "|" + str(record.description)
      out_line = out_line + "|" + str(record.type)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()

  # ----------------------------------- Podcast ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PODCAST_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Podcast.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.image)
      out_line = out_line + "|" + str(record.playlist)
      out_line = out_line + "|" + str(record.country)
      out_line = out_line + "|" + str(record.description)
      out_line = out_line + "|" + str(record.style)
      out_line = out_line + "|" + str(record.stars)
      out_line = out_line + "|" + str(record.feed_url)
      out_line = out_line + "|" + str(record.feed_filter)
      out_line = out_line + "|" + str(record.pod_dir)
      out_line = out_line + "|" + str(record.publisher)
      out_line = out_line + "|" + str(record.priority)
      out_line = out_line + "|" + str(record.fav)
      out_line = out_line + "|" + str(record.retag)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()

  # ----------------------------------- Artist Link ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_ARTIST_LINK_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Artist_Link.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.url)
      out_line = out_line + "|" + str(record.artist_id)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()

  # ----------------------------------- Radio Link ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_RADIO_LINK_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Radio_Link.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.url)
      out_line = out_line + "|" + str(record.radio_id)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()

  # ----------------------------------- Podcast Link ---------------------------------------

    csv_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_PODCAST_LINK_TABLE_FILE)

    f = open(csv_file,"w")

    record_list = Podcast_Link.query.all()

    for record in record_list:
      out_line = str(record.id)
      out_line = out_line + "|" + str(record.name)
      out_line = out_line + "|" + str(record.url)
      out_line = out_line + "|" + str(record.podcast_id)

      out_line = out_line.encode('utf-8')

      f.write(out_line + "\n")

    f.close()


