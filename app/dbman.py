
import os

from . import db
from . import CONFIG
from .models import Radios, Program, Artist, Playlist, Podcast, Artist_Link, Radio_Link, Podcast_Link, Bookmark, Preset

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
    elif table_name == 'Bookmark':
      return self.db.session.query(Bookmark).count()
    elif table_name == 'Preset':
      return self.db.session.query(Preset).count()

  def csv_file(self, table_name):

    return os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_CSV_DIR, CONFIG.CSV_TABLE_FILE[table_name])

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
    log_message = "{} -> {} [{}]"

  # ----------------------------------- Radio ---------------------------------------
    table_name = 'Radios'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Radios.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.url,
        record.image,
        record.country,
        record.num_plays,
        record.style,
        record.stars,
        record.fav,
        record.description
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Program ---------------------------------------
    table_name = 'Program'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")
    
    record_list = Program.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.times,
        record.week_days,
        record.description,
        record.style,
        record.stars,
        record.fav,
        record.twitter,
        record.radio_id 
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Artist ---------------------------------------
    table_name = 'Artist'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")
    
    record_list = Artist.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.image,
        record.country,
        record.description,
        record.style,
        record.stars,
        record.fav
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Playlist ---------------------------------------
    table_name = 'Playlist'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Playlist.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.image,
        record.playlist,
        record.description,
        record.type
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Podcast ---------------------------------------
    table_name = 'Podcast'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Podcast.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.image,
        record.playlist,
        record.country,
        record.description,
        record.style,
        record.stars,
        record.feed_url,
        record.feed_filter,
        record.pod_dir,
        record.publisher,
        record.priority,
        record.fav,
        record.retag
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Radio Link ---------------------------------------
    table_name = 'Radio_Link'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Radio_Link.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.url,
        record.radio_id
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Artist Link ---------------------------------------
    table_name = 'Artist_Link'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Artist_Link.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.url,
        record.artist_id
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Podcast Link ---------------------------------------
    table_name = 'Podcast_Link'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Podcast_Link.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}\n""".format(
        record.id, 
        record.name, 
        record.url,
        record.podcast_id
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  # ----------------------------------- Bookmark ---------------------------------------
    table_name = 'Bookmark'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Bookmark.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}\n""".format(
        record.id, 
        record.url, 
        record.image_url,
        record.priority
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))

  # ----------------------------------- Preset ---------------------------------------
    table_name = 'Preset'
    csv_file = self.csv_file(table_name)

    f = open(csv_file,"w")

    record_list = Preset.query.all()

    for record in record_list:
      out_line = u"""{}|{}|{}|{}|{}\n""".format(
        record.id,
        record.name,
        record.description,
        record.url,
        record.radio_id
      )

      out_line = out_line.encode('utf-8')

      f.write(out_line)

    f.close()

    print log_message.format(table_name, csv_file, len(record_list))
  ################################################################################################################################################################
  # Import Data
  ################################################################################################################################################################

  def import_csv_data(self):

    print "===> Importing Tables from Files"
    log_message = "{} [{}]"

  # ----------------------------------- Radios ---------------------------------------
    table_name = 'Radios'
    csv_file = self.csv_file(table_name)

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

        record = Radios(
          id=id,
          name=name,
          url=url,
          image=image,
          country=country,
          num_plays=num_plays,
          style=style,
          stars=stars,
          fav=fav,
          description=description
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

# ----------------------------------- Program ---------------------------------------
    table_name = 'Program'
    csv_file = self.csv_file(table_name)

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

        record = Program(
          id=id,
          name=name,
          times=times,
          week_days=week_days,
          description=description,
          style=style,
          stars=stars,
          fav=fav,
          twitter=twitter,
          radios=radio
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

# ----------------------------------- Artist ---------------------------------------
    table_name = 'Artist'
    csv_file = self.csv_file(table_name)

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

        record = Artist(
          id=id,
          name=name,
          image=image,
          country=country,
          description=description,
          style=style,
          stars=stars
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

  # ----------------------------------- Playlist ---------------------------------------
    table_name = 'Playlist'
    csv_file = self.csv_file(table_name)

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

        record = Playlist(
          id=id,
          name=name,
          image=image,
          playlist=playlist,
          description=description,
          type=type
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)
  
  # ----------------------------------- Podcast ---------------------------------------
    table_name = 'Podcast'
    csv_file = self.csv_file(table_name)

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
        
        priority_txt = words[12]
        if (priority_txt == 'None') or (priority_txt == ''):
          priority = 0
        else:
          priority = int(priority_txt)

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


        record = Podcast(
          id=id,
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
          retag=retag
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

  # ----------------------------------- Radio Links ---------------------------------------
    table_name = 'Radio_Link'
    csv_file = self.csv_file(table_name)

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

        record = Radio_Link(
          id=id,
          name=name,
          url=url,
          radios=radio
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

# ----------------------------------- Artist Links ---------------------------------------
    table_name = 'Artist_Link'
    csv_file = self.csv_file(table_name)

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

        record = Artist_Link(
          id=id,
          name=name,
          url=url,
          artist=artist
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

  # ----------------------------------- Podcast Links ---------------------------------------
    table_name = 'Podcast_Link'
    csv_file = self.csv_file(table_name)

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

        record = Podcast_Link(
          id=id,
          name=name,
          url=url,
          podcast=podcast
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

  # ----------------------------------- Bookmark  ---------------------------------------
    table_name = 'Bookmark'
    csv_file = self.csv_file(table_name)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        url = words[1].decode('utf-8')
        image_url = words[2].decode('utf-8')
        priority = int(words[3])

        record = Bookmark(
          id=id,
          url=url,
          image_url=image_url,
          priority=priority
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)

  # ----------------------------------- Bookmark  ---------------------------------------
    table_name = 'Preset'
    csv_file = self.csv_file(table_name)

    with open(csv_file,"r") as csv:
      csv_data = csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        id = int(words[0])
        name = words[1].decode('utf-8')
        description = words[2].decode('utf-8')
        url = words[3].decode('utf-8')
        radio_id = int(words[4])

        radio = Radios.query.filter_by(id=radio_id).first()

        record = Preset(
          id=id,
          name=name,
          description=description,
          url=url,
          radios=radio
        )

        db.session.add(record)
        db.session.commit()

    csv.close()

    record_cout = self.count_records(table_name)
    print log_message.format(table_name, record_cout)
