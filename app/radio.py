import os, sys
import time

from sqlalchemy import desc

from mpd import MPDClient

from .models import Radios,Program,Artist,Playlist,Podcast, Bookmark
from . import CONFIG

################################################################################################################################################################
# Radio Player
################################################################################################################################################################

class RadioPlayer:
      mpd_client = CONFIG.DEFAULT_MPD_CLIENT
      mpd_port = CONFIG.DEFAULT_MPD_PORT
      mpd_servers = CONFIG.MPD_SERVERS
      client = MPDClient()
      bookmark_list = []
      state = ''
      loaded = ''
      radio = Radios()
      playlist = Playlist()
      artist = Artist()
      podcast = Podcast()
      album = ''
      player_img = ''

      def __init__(self):
          self.client = MPDClient()
          self.client.connect(self.mpd_client, self.mpd_port)
          self.state = 'stop'
          self.loaded = 'none'
          self.player_img = '/static/images/radios/empty.png'
          self.client.close()
          self.client.disconnect()

      def connect(self,hostname):
          self.mpd_client = hostname
          self.client.disconnect()
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.disconnect()

      def disconnect(self):
          self.client.disconnect()

################################################################################################################################################################
# Player
################################################################################################################################################################

      def play_url(self,url):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.clear()
          self.client.add(url)
          self.client.play(0)
          self.client.close()
          self.client.disconnect()

          self.loaded = 'url'
          self.state = 'play'
          self.album = ''
          self.player_img = '/static/images/radios/empty.png'

      def playradio(self,radio):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.clear()
          self.client.add(radio.url)
          self.client.play(0)
          self.client.close()
          self.client.disconnect()

          self.loaded = 'radio'
          self.state = 'play'
          self.radio = radio
          self.album = ''
          self.player_img = '/static/images/radios/' + radio.image

      def play(self):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.play()
          self.client.close()
          self.client.disconnect()
          self.state = 'play'

      def stop(self):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.stop()
          self.client.close()
          self.client.disconnect()
          self.state = 'stop'

      def pause(self):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.pause()
          self.client.close()
          self.client.disconnect()
          self.state = 'pause'

      def next(self):
          if self.loaded in ['album','playlist','podcast']:

            self.client.connect(self.mpd_client, self.mpd_port)

            pos = int(self.client.currentsong()['pos'])
            playlist_len = int(self.client.status()['playlistlength'])

            if pos < (playlist_len - 1):
              self.client.next()
              
            self.client.close()
            self.client.disconnect()

      def previous(self):
        if self.loaded in ['album','playlist','podcast']:
        
          self.client.connect(self.mpd_client, self.mpd_port)

          pos = int(self.client.currentsong()['pos'])
          playlist_len = int(self.client.status()['playlistlength'])

          if pos > 0:
            self.client.previous()
          
          self.client.close()
          self.client.disconnect()

      def play_song(self,pos):
          self.client.connect(self.mpd_client, self.mpd_port)

          self.client.play(pos)

          self.client.close()
          self.client.disconnect()
          
          self.state = 'play'

      def seekcur(self,time):
        self.client.connect(self.mpd_client, self.mpd_port)

        self.client.seekcur(time)

        self.client.close()
        self.client.disconnect()

      def seekplus(self,time_interval):
        self.client.connect(self.mpd_client, self.mpd_port)

        elapsed_time = float(self.client.status()['elapsed'])
        self.client.seekcur(elapsed_time + float(time_interval))
        
        self.client.close()
        self.client.disconnect()

      def seekless(self,time_interval):
        self.client.connect(self.mpd_client, self.mpd_port)
        
        elapsed_time = float(self.client.status()['elapsed'])
        self.client.seekcur(elapsed_time - float(time_interval))
        
        self.client.close()
        self.client.disconnect()

      def elapsed_time(self):
        self.client.connect(self.mpd_client, self.mpd_port)
        
        elapsed_time = float(self.client.status()['elapsed'])
        
        self.client.close()
        self.client.disconnect()   

        return elapsed_time    

################################################################################################################################################################
# Status
################################################################################################################################################################

      def update_state(self,radio_list):
          self.client.connect(self.mpd_client, self.mpd_port)

          self.state = self.client.status()['state']
          current_song = self.client.currentsong()

          self.client.close()
          self.client.disconnect()

          if (len(current_song)==0):
            self.loaded='none'
            self.status='stop'
          else:
            if (self.loaded == 'radio'):
              current_link = current_song['file']
              for radio in radio_list:
                  if radio.url == current_link:
                      self.radio = radio


      def update_bookmarks(self):

          self.bookmark_list = Bookmark.query.order_by(Bookmark.priority).all()


      def server_currentsong(self,key_value):

          self.client.connect(self.mpd_client, self.mpd_port)

          currentsong = self.client.currentsong()
                    
          self.client.close()
          self.client.disconnect()

          if key_value in currentsong:
            if key_value in ['pos']:
              return int(currentsong[key_value])
            else:
              return currentsong[key_value]
          else:
            return ''


      def server_status(self,key_value):

          self.client.connect(self.mpd_client, self.mpd_port)

          status = self.client.status()
                    
          self.client.close()
          self.client.disconnect()

          if key_value in status:
            return status[key_value]
          else:
            return ''


      def elapsed_time_str(self):
        self.client.connect(self.mpd_client, self.mpd_port)
        elapsed_time = round(float(self.client.status()['elapsed']))

        m,s = divmod(int(elapsed_time),60)

        elapsed_time_str = '{:d}:{:02d}'.format(m,s)

        self.client.close()
        self.client.disconnect()   

        return elapsed_time_str    


      def play_progress(self):
        self.client.connect(self.mpd_client, self.mpd_port)
        elapsed_time = round(float(self.client.status()['elapsed']))
        song_time = round(float(self.client.currentsong()['time']))

        play_progress = 100 * elapsed_time / song_time

        play_progress_str = str(play_progress) + '%'

        self.client.close()
        self.client.disconnect()   

        return play_progress_str   


################################################################################################################################################################
# Playlist
################################################################################################################################################################


      def playlist_songs(self,playlist_name):

          self.client.connect(self.mpd_client, self.mpd_port)

          songs_list = []
          pos = 0
          playlist_info = self.client.listplaylistinfo(playlist_name)

          for info in playlist_info:

            if 'time' in info:
              m, s = divmod(int(info['time']), 60)
              if m > 60:
                h, m = divmod(m, 60)
                time = '{}:{:02d}:{:02d}'.format(h,m,s)
              else:
                time = '{}:{:02d}'.format(m,s)
         
            else:
              time = ''

            if 'title' in info:
              title = info['title']
            elif 'file' in info:
              filename = info['file']
              title = filename.split('/')[-1]
            else:
              title = ''
            
            if 'artist' in info:
              artist = info['artist']
            else:
              artist = playlist_name

            songs_list.append({'pos':pos,'title':title,'artist':artist,'track':pos+1,'time':time})
            pos = pos + 1

          self.client.close()
          self.client.disconnect()

          songs_list.sort(key=lambda x: x['title'], reverse=True)

          return songs_list

      def load_playlist(self,playlist_name):

          self.client.connect(self.mpd_client, self.mpd_port)

          playlist = Playlist.query.filter_by(playlist=playlist_name).first()

          self.client.clear()
          self.client.load(playlist_name)
          self.client.play()

          self.loaded = 'playlist'
          self.state = 'play'
          self.playlist = playlist
          self.album = ''
          self.player_img = '/static/images/playlists/' + playlist.image

          self.client.close()
          self.client.disconnect()


      def playlist_info(self):
          self.client.connect(self.mpd_client, self.mpd_port)

          pl_info = self.client.playlistinfo()

          self.client.close()
          self.client.disconnect()

          return pl_info

      def current_playlist_songs(self):

          self.client.connect(self.mpd_client, self.mpd_port)

          songs_list = []
          pos = 0
          currnet_playlist = self.client.playlistinfo()

          for info in currnet_playlist:

              if self.loaded=='radio':
                  time = 0
                  title = info['name']
              else:
                  m, s = divmod(int(info['time']), 60)
                  if  s < 10:
                      time = str(m) + ":0" + str(s)
                  else:
                      time = str(m) + ":" + str(s)

                  title = info['title']

              songs_list.append({'pos':pos,'title':title,'track':pos+1,'time':time})
              pos = pos + 1

          self.client.close()
          self.client.disconnect()

          return songs_list

################################################################################################################################################################
# Artist and Album
################################################################################################################################################################

      # ---> List Albums for an Artist order by Date
      def artist_albums(self,artist):
          self.client.connect(self.mpd_client, self.mpd_port)

          album_list = self.client.list('album','artist',artist.name)

          album_info = []
          for album in album_list:
            alb_date = self.client.list('date','artist',artist.name,'album',album)
            album_info.append({'album':album,'date':alb_date[0]})

          self.client.close()
          self.client.disconnect()

          album_info.sort(key=lambda x: x['date'])

          return album_info


      def album_info(self, artist, album):
        self.client.connect(self.mpd_client, self.mpd_port)

        album_info = self.client.find('album',album,'artist',artist.name)[0]

        self.client.close()
        self.client.disconnect()

        return album_info


      def album_songs(self,artist,album):
        self.client.connect(self.mpd_client, self.mpd_port)

        songs_list = []
        pos = 0
        find_res = self.client.find('album',album,'artist',artist.name)

        for res in find_res:

          m, s = divmod(int(res['time']), 60)
          if  s < 10:
            time = str(m) + ":0" + str(s)
          else:
            time = str(m) + ":" + str(s)

          songs_list.append({'pos':pos,'title':res['title'],'track':pos+1,'time':time})
          pos = pos + 1

        self.client.close()
        self.client.disconnect()

        return songs_list

      def load_album(self,artist,album):
          self.client.connect(self.mpd_client, self.mpd_port)

          songs_list = self.client.find('album',album,'artist',artist.name)

          self.client.clear()

          for song in songs_list:
              self.client.add(song['file'])

          self.client.play()

          self.loaded = 'album'
          self.state = 'play'
          self.artist = artist
          self.album = album
          self.player_img = '/static/images/albums/' + str(artist.name) + '/' + str(album) + '.png'

          self.client.close()
          self.client.disconnect()

          return songs_list


      def load_podcast(self,podcast):
          self.client.connect(self.mpd_client, self.mpd_port)

          self.client.clear()
          self.client.load(podcast.playlist)
          self.client.play()

          self.loaded = 'podcast'
          self.state = 'play'
          self.podcast = podcast
          self.player_img = '/static/images/playlists/' + podcast.image

          self.client.close()
          self.client.disconnect()


      def play_podcast_url(self,podcast,url):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.clear()
          self.client.add(url)
          self.client.play(0)
          self.client.close()
          self.client.disconnect()

          self.loaded = 'podcast-url'
          self.state = 'play'
          self.podcast = podcast
          self.player_img = '/static/images/playlists/' + podcast.image

      def outputs(self):
          self.client.connect(self.mpd_client, self.mpd_port)
          
          output_list = self.client.outputs()

          self.client.close()
          self.client.disconnect()

          names = []
          for output in output_list:
            names.append(output['outputname'])

          return output_list


      def toggle_output(self,id):
          self.client.connect(self.mpd_client, self.mpd_port)
          
          self.client.toggleoutput(id)

          self.client.close()
          self.client.disconnect()


################################################################################################################################################################
# Program Info
################################################################################################################################################################

class ProgramsInfo:
  radio = Radios()
  program = Program()
  week_day_letters = ['Lun','Mar','Mie','Jue','Vie','Sab','Dom']
  timezone = 0
  week_day = 0
  list_week_day = 0

  def __init__(self,radio):
    self.radio = radio
    self.timezone = self.timezone()
    self.week_day = self.act_week_day()
    self.list_week_day = self.week_day
    self.program_update()

  # ---> Set Week Day
  def week_day_letter(self,wday):

    if int(wday) in [0,1,2,3,4,5,6]:
      return self.week_day_letters[int(wday)]

  # ---> Set Week Day
  def set_list_week_day(self,wday):

    if int(wday) in [0,1,2,3,4,5,6]:
      self.list_week_day = wday

  # ---> Progams List
  def program_list(self):

    self.radio.program_list.sort(key=lambda x: x.times)

    return self.radio.program_list

  # ---> TimeZone
  def timezone(self):

    if self.radio.country in CONFIG.TIMEZONES:
      timezone = CONFIG.TIMEZONES[self.radio.country]
    else:
      timezone = 0

    return timezone
      
  # ---> Actual Week Day
  def act_hour(self):
        
    act_hour = int(time.localtime().tm_hour) + self.timezone
    act_hour = act_hour % 24
        
    return act_hour

  # ---> Actual Week Day
  def act_week_day(self):
        
    act_wday = time.localtime().tm_wday
    act_hour = int(time.localtime().tm_hour) + self.timezone

    if act_hour < 0:
      act_wday = act_wday - 1
    if act_hour > 23:
      act_wday = act_wday + 1
        
    return act_wday

  # ---> Radio Time
  def radio_time_day(self):

    act_wday = self.act_week_day()

    act_h = self.act_hour()
    if act_h < 10:
      act_h_txt = '0' + str(act_h)
    else:
      act_h_txt = str(act_h)

    act_m = int(time.localtime().tm_min)
    if act_m < 10:
      act_m_txt = '0' + str(act_m)
    else:
      act_m_txt = str(act_m)

    str_h = act_h_txt + ':' + act_m_txt + ' [ ' + self.week_day_letter(act_wday) + ' ]'

    return str_h


  # ---> Check if Program is Live
  def is_prog_today(self,program):

    prog_wdays = program.week_days.split(',')
        
    return (str(self.list_week_day) in prog_wdays)


  # ---> Check Program Live
  def is_prog_live(self,program):

    act_h = self.act_hour()

    act_m = int(time.localtime().tm_min)
    act_day_m = act_h * 60 + act_m

    prog_wdays = program.week_days.split(',')

    prog_ini_h = int(program.times.split('-')[0].split(':')[0])
    prog_ini_m = int(program.times.split('-')[0].split(':')[1])

    prog_end_h = int(program.times.split('-')[1].split(':')[0])
    prog_end_m = int(program.times.split('-')[1].split(':')[1])

    prog_day_ini_m = prog_ini_h * 60 + prog_ini_m
    prog_day_end_m = prog_end_h * 60 + prog_end_m

    return ( (str(self.act_week_day()) in prog_wdays) and (act_day_m >= prog_day_ini_m) and (act_day_m < prog_day_end_m) )

  # ---> Program Time
  def program_update(self):

    self.program = None

    for program in self.radio.program_list:
      if self.is_prog_live(program):
        self.program = program

  
  # ---> Program Time
  def program_time(self):

    self.program_update()

    if self.program:
      prog_ini_h = int(self.program.times.split('-')[0].split(':')[0])
      prog_ini_m = int(self.program.times.split('-')[0].split(':')[1])

      prog_end_h = int(self.program.times.split('-')[1].split(':')[0])
      prog_end_m = int(self.program.times.split('-')[1].split(':')[1])

      prog_day_ini_m = prog_ini_h * 60 + prog_ini_m
      prog_day_end_m = prog_end_h * 60 + prog_end_m

      prog_time_s = (prog_day_end_m - prog_day_ini_m) * 60
        
      return prog_time_s

    else:

      return 0


  # ---> Program Elapsed Time
  def program_elapsed_time(self):

    self.program_update()

    if self.program:
      act_h = self.act_hour()
      act_m = int(time.localtime().tm_min)

      act_day_m = act_h * 60 + act_m

      prog_ini_h = int(self.program.times.split('-')[0].split(':')[0])
      prog_ini_m = int(self.program.times.split('-')[0].split(':')[1])

      prog_day_ini_m = prog_ini_h * 60 + prog_ini_m

      prog_elapsed_time_s = (act_day_m - prog_day_ini_m) * 60
          
      return prog_elapsed_time_s

    else:

      return 0
