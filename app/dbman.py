
import os

from . import db
from . import global_values
from .models import Radios, Artist, Playlist, Podcast

class DBManager():

  db

  def __init__(self,db):
    self.db = db

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

  # ----------------------------------- Radio ---------------------------------------

    radio_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_radios_table_file)

    with open(radio_file,"r") as radio_csv:

      csv_data = radio_csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        nickname = words[0]
        name = words[1].decode('utf-8')
        url = words[2]
        country = words[3].decode('utf-8')
        num_plays = words[4]
        style = words[5].decode('utf-8')
        stars = words[6]
        web_url = words[7]
        twitter = words[8]

        radio_record = Radios(nickname=nickname,
                              name=name,
                              url=url,
                              country=country,
                              num_plays=num_plays,
                              style=style,
                              stars=stars,
                              web_url=web_url,
                              twitter=twitter)

        db.session.add(radio_record)
        db.session.commit()

    radio_csv.close()

  # ----------------------------------- Playlist ---------------------------------------

    playlist_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_playlist_table_file)

    with open(playlist_file,"r") as playlist_csv:
      csv_data = playlist_csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        name = words[0].decode('utf-8')
        image = words[1].decode('utf-8')
        playlist = words[2].decode('utf-8')
        description = words[3].decode('utf-8')
        type = words[4].decode('utf-8')

        playlist_record = Playlist(name=name,
                                  image=image,
                                  playlist=playlist,
                                  description=description,
                                  type=type)

        db.session.add(playlist_record)
        db.session.commit()

    playlist_csv.close()

  # ----------------------------------- Artist ---------------------------------------

    artist_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_artist_table_file)

    with open(artist_file,"r") as artist_csv:
      csv_data = artist_csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        name = words[0].decode('utf-8')
        image = words[1].decode('utf-8')
        country = words[2].decode('utf-8')
        description = words[3].decode('utf-8')
        style = words[4].decode('utf-8')
        stars = words[5]

        artist_record = Artist(name=name,
                              image=image,
                              country=country,
                              description=description,
                              style=style,
                              stars=stars)

        db.session.add(artist_record)
        db.session.commit()

    artist_csv.close()

  # ----------------------------------- Podcast ---------------------------------------

    podcast_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_podcast_table_file)

    with open(podcast_file,"r") as podcast_csv:
      csv_data = podcast_csv.readlines()

      for line in csv_data:
        line = line.rstrip()
        words = line.split("|")

        name = words[0].decode('utf-8')
        image = words[1].decode('utf-8')
        playlist = words[2].decode('utf-8')
        country = words[3].decode('utf-8')
        description = words[4].decode('utf-8')
        style = words[5].decode('utf-8')
        stars = words[6]
        web_url = words[7]
        feed_url = words[8]
        pod_dir = words[9]
        feed_filter = words[10]
        publisher = words[11].decode('utf-8')
        priority = words[12]

        podcast_record = Podcast(name=name,
                                image=image,
                                playlist=playlist,
                                country=country,
                                description=description,
                                style=style,stars=stars,
                                web_url=web_url,
                                feed_url=feed_url,
                                pod_dir=pod_dir,
                                feed_filter=feed_filter,
                                publisher=publisher,
                                priority=priority)

        db.session.add(podcast_record)
        db.session.commit()

    podcast_csv.close()

  ################################################################################################################################################################
  # Export Data
  ################################################################################################################################################################

  def export_csv_data(self):

   # ----------------------------------- Radio ---------------------------------------

    radio_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_radios_table_file)

    f_radio = open(radio_file,"w")

    radio_list = Radios.query.all()

    for radio in radio_list:
      out_line = radio.nickname
      out_line = out_line + "|" + radio.name
      out_line = out_line + "|" + radio.url
      out_line = out_line + "|" + radio.country
      out_line = out_line + "|" + str(radio.num_plays)
      out_line = out_line + "|" + radio.style
      out_line = out_line + "|" + str(radio.stars)
      out_line = out_line + "|" + radio.web_url
      out_line = out_line + "|" + radio.twitter

      out_line = out_line.encode('utf-8')

      f_radio.write(out_line + "\n")

    f_radio.close()

  # ----------------------------------- Playlist ---------------------------------------

    playlist_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_playlist_table_file)

    f_playlist = open(playlist_file,"w")

    playlist_list = Playlist.query.all()

    for playlist in playlist_list:
      out_line = playlist.name
      out_line = out_line + "|" + playlist.image
      out_line = out_line + "|" + playlist.playlist
      out_line = out_line + "|" + str(playlist.description)
      out_line = out_line + "|" + str(playlist.type)

      out_line = out_line.encode('utf-8')

      f_playlist.write(out_line + "\n")

    f_playlist.close()


  # ----------------------------------- Artist ---------------------------------------

    artist_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_artist_table_file)

    f_artist = open(artist_file,"w")

    artist_list = Artist.query.all()

    for artist in artist_list:
      out_line = artist.name
      out_line = out_line + "|" + artist.image
      out_line = out_line + "|" + artist.country
      out_line = out_line + "|" + artist.description
      out_line = out_line + "|" + artist.style
      out_line = out_line + "|" + str(artist.stars)

      out_line = out_line.encode('utf-8')

      f_artist.write(out_line + "\n")

    f_artist.close()

  # ----------------------------------- Podcast ---------------------------------------

    podcast_file = os.path.join(global_values.project_root_dir, global_values.project_db_dir, global_values.csv_podcast_table_file)

    f_podcast = open(podcast_file,"w")

    podcast_list = Podcast.query.all()

    for podcast in podcast_list:
      out_line = podcast.name
      out_line = out_line + "|" + podcast.image
      out_line = out_line + "|" + podcast.playlist
      out_line = out_line + "|" + podcast.country
      out_line = out_line + "|" + podcast.description
      out_line = out_line + "|" + podcast.style
      out_line = out_line + "|" + str(podcast.stars)
      out_line = out_line + "|" + podcast.web_url
      out_line = out_line + "|" + podcast.feed_url
      out_line = out_line + "|" + podcast.pod_dir
      out_line = out_line + "|" + podcast.feed_filter
      out_line = out_line + "|" + podcast.publisher
      out_line = out_line + "|" + str(podcast.priority)

      out_line = out_line.encode('utf-8')

      f_podcast.write(out_line + "\n")

    f_podcast.close()

