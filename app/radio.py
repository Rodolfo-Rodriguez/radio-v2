import os, sys
import time
import requests 

from sqlalchemy import desc

from mpd import MPDClient

from .models import Radios,Program,Artist,Playlist,Podcast, Bookmark
from . import CONFIG

################################################################################################################################################################
# Radio Player
################################################################################################################################################################

class RadioPlayer:
  server_name = CONFIG.DEFAULT_SERVER_NAME
  server_port = CONFIG.DEFAULT_SERVER_PORT
  server_type = CONFIG.DEFAULT_SERVER_TYPE
  mpd_client = MPDClient()

  server_names = CONFIG.SERVER_NAMES
      
  bookmark_list = []
  bookmark_max = CONFIG.BOOKMARK_MAX

  state = ''
  loaded = ''
  album = ''
  player_img = ''

  radio = Radios()
  playlist = Playlist()
  artist = Artist()
  podcast = Podcast()

  def __init__(self):
    self.state = 'stop'
    self.loaded = 'none'
    self.player_img = '/static/images/radios/empty.png'

################################################################################################################################################################
# Server
################################################################################################################################################################

  def update_server_type(self,hostname):
    if hostname in CONFIG.MPD_SERVERS:
      self.server_type = 'MPD'
    else:
      self.server_type = 'CXN'

  def select_server(self,hostname):
    self.server_name = hostname
    self.server_port = CONFIG.SERVER_PORTS[hostname]
    self.update_server_type(hostname)

  def server_connect(self):
    if self.server_type == 'MPD':
      self.mpd_client.connect(self.server_name, self.server_port)

  def server_disconnect(self):
    if self.server_type == 'MPD':
      self.mpd_client.close()
      self.mpd_client.disconnect()

  def current_server(self):
    return self.server_names[self.server_name]

################################################################################################################################################################
# Player
################################################################################################################################################################

  def play_url(self,url):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.add(url)
      self.mpd_client.play(0)
      self.server_disconnect()

      self.loaded = 'url'
      self.state = 'play'
      self.album = ''
      self.player_img = '/static/images/radios/empty.png'

  def playradio(self,radio):
    play_ok = False
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.add(radio.url)
      self.mpd_client.play(0)
      self.server_disconnect()
      play_ok = True
    else:
      if (radio.preset > 0) and (radio.preset < 21):
        self.cxn_play_preset(radio.preset)
        play_ok = True

    if play_ok:
      self.loaded = 'radio'
      self.state = 'play'
      self.radio = radio
      self.album = ''
      self.player_img = '/static/images/radios/' + radio.image

  def play_pause(self):
    if self.state == 'play':
      self.state = 'pause'
    else:
      self.state = 'play'          

    if (self.server_type == 'MPD'):
      self.server_connect()          
      if self.state == 'play':
        self.mpd_client.pause()
      else:
        self.mpd_client.play()
      self.server_disconnect()
    else:
      self.cxn_play_remote('PLAY_PAUSE')
          
  def play(self):
    self.state = 'play'
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.play()
      self.server_disconnect()
    else:
      self.cxn_play_remote('PLAY_PAUSE')

  def stop(self):
    self.state = 'stop'
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.stop()
      self.server_disconnect()
    else:
      self.cxn_play_remote('STOP')

  def pause(self):
    self.state = 'pause'
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.pause()
      self.server_disconnect()
    else:
      self.cxn_play_remote('PLAY_PAUSE')

  def next(self):
    if self.loaded in ['album','playlist','podcast']:
      if (self.server_type == 'MPD'):
        self.server_connect()
        pos = int(self.mpd_client.currentsong()['pos'])
        playlist_len = int(self.mpd_client.status()['playlistlength'])      
        if pos < (playlist_len - 1):
          self.mpd_client.next()
        self.server_disconnect()
      else:
        self.cxn_play_remote('NEXT')

  def previous(self):
    if self.loaded in ['album','playlist','podcast']:
      if (self.server_type == 'MPD'):
        self.server_connect()
        pos = int(self.mpd_client.currentsong()['pos'])
        playlist_len = int(self.mpd_client.status()['playlistlength'])
        if pos > 0:
          self.mpd_client.previous()
        self.server_disconnect()
      else:
        self.cxn_play_remote('PREVIOUS')

  def play_song(self,pos):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.play(pos)
      self.server_disconnect()
      self.state = 'play'

  def seekcur(self,time):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.seekcur(time)
      self.server_disconnect()

  def seekplus(self,time_interval):
    if (self.server_type == 'MPD'):
      self.server_connect()
      elapsed_time = float(self.mpd_client.status()['elapsed'])
      self.mpd_client.seekcur(elapsed_time + float(time_interval))
      self.server_disconnect()

  def seekless(self,time_interval):
    if (self.server_type == 'MPD'):
      self.server_connect()
      elapsed_time = float(self.mpd_client.status()['elapsed'])
      self.mpd_client.seekcur(elapsed_time - float(time_interval))
      self.server_disconnect()

  def elapsed_time(self):
    if (self.server_type == 'MPD'):
      self.server_connect()
      elapsed_time = float(self.mpd_client.status()['elapsed'])
      self.server_disconnect()

      return elapsed_time

################################################################################################################################################################
# Status
################################################################################################################################################################

  def update_state(self,radio_list):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.state = self.mpd_client.status()['state']
      current_song = self.mpd_client.currentsong()
      self.server_disconnect()

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
    self.bookmark_list = Bookmark.query.order_by(Bookmark.priority).all()[0:self.bookmark_max]

  def server_currentsong(self,key_value):
    if (self.server_type == 'MPD'):
      self.server_connect()
      currentsong = self.mpd_client.currentsong()
      self.server_disconnect()
      if key_value in currentsong:
        if key_value in ['pos']:
          return int(currentsong[key_value])
        else:
          return currentsong[key_value]
      else:
        return ''
    else:
      return ''

  def server_status(self,key_value):
    if (self.server_type == 'MPD'):
      self.server_connect()
      status = self.mpd_client.status()
      self.server_disconnect()
      if key_value in status:
        return status[key_value]
      else:
        return ''
    else:
      return ''

  def elapsed_time_str(self):
    if (self.server_type == 'MPD'):
      self.server_connect()
      elapsed_time = round(float(self.mpd_client.status()['elapsed']))
      m,s = divmod(int(elapsed_time),60)
      elapsed_time_str = '{:d}:{:02d}'.format(m,s)
      self.server_disconnect()
      return elapsed_time_str  
    else:
      return 0  

  def play_progress(self):
    if (self.server_type == 'MPD'):
      self.server_connect()
      elapsed_time = round(float(self.mpd_client.status()['elapsed']))
      song_time = round(float(self.mpd_client.currentsong()['time']))
      play_progress = 100 * elapsed_time / song_time
      play_progress_str = str(play_progress) + '%'
      self.server_disconnect()
      return play_progress_str
    else:
      return ''

################################################################################################################################################################
# Playlist
################################################################################################################################################################

  def playlist_songs(self,playlist_name):
    songs_list = []
    pos = 0
    
    if (self.server_type == 'MPD'):
      self.server_connect()
      playlist_info = self.mpd_client.listplaylistinfo(playlist_name)
      self.server_disconnect()

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

      songs_list.sort(key=lambda x: x['title'], reverse=True)

    return songs_list

  def load_playlist(self,playlist_name):
    if (self.server_type == 'MPD'):
      self.server_connect()
      playlist = Playlist.query.filter_by(playlist=playlist_name).first()
      self.mpd_client.clear()
      self.mpd_client.load(playlist_name)
      self.mpd_client.play()
      self.server_disconnect()

      self.loaded = 'playlist'
      self.state = 'play'
      self.playlist = playlist
      self.album = ''
      self.player_img = '/static/images/playlists/' + playlist.image

  def playlist_info(self):
    if (self.server_type == 'MPD'):
      self.server_connect()
      pl_info = self.mpd_client.playlistinfo()
      self.server_disconnect()
      return pl_info
    else:
      return ''

  def current_playlist_songs(self):
    songs_list = []
    pos = 0
    if (self.server_type == 'MPD'):
      self.server_connect()
      currnet_playlist = self.mpd_client.playlistinfo()
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
      self.server_disconnect()

    return songs_list

################################################################################################################################################################
# Artist and Album
################################################################################################################################################################

# ---> List Albums for an Artist order by Date
  def artist_albums(self,artist):
    album_info = []
    
    if (self.server_type == 'MPD'):
      self.server_connect()
      album_list = self.mpd_client.list('album','artist',artist.name)
      for album in album_list:
        alb_date = self.mpd_client.list('date','artist',artist.name,'album',album)
        album_info.append({'album':album,'date':alb_date[0]})
      self.server_disconnect()
      album_info.sort(key=lambda x: x['date'])

    return album_info

  def album_info(self, artist, album):
    if (self.server_type == 'MPD'):
      self.server_connect()
      album_info = self.mpd_client.find('album',album,'artist',artist.name)[0]
      self.server_disconnect()
      return album_info
    else:
      return ''

  def album_songs(self,artist,album):
    songs_list = []
    pos = 0
    
    if (self.server_type == 'MPD'):
      self.server_connect()
      find_res = self.mpd_client.find('album',album,'artist',artist.name)
      for res in find_res:
        m, s = divmod(int(res['time']), 60)
        if  s < 10:
          time = str(m) + ":0" + str(s)
        else:
          time = str(m) + ":" + str(s)
        songs_list.append({'pos':pos,'title':res['title'],'track':pos+1,'time':time})
        pos = pos + 1
      self.server_disconnect()

    return songs_list

  def load_album(self,artist,album):
    songs_list = []

    if (self.server_type == 'MPD'):
      self.server_connect()
      songs_list = self.mpd_client.find('album',album,'artist',artist.name)
      self.mpd_client.clear()
      for song in songs_list:
        self.mpd_client.add(song['file'])      
      self.mpd_client.play()

      self.loaded = 'album'
      self.state = 'play'
      self.artist = artist
      self.album = album
      self.player_img = '/static/images/albums/' + str(artist.name) + '/' + str(album) + '.png'
      
      self.server_disconnect()
    
    return songs_list

  def load_podcast(self,podcast):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.load(podcast.playlist)
      self.mpd_client.play()

      self.loaded = 'podcast'
      self.state = 'play'
      self.podcast = podcast
      self.player_img = '/static/images/playlists/' + podcast.image

      self.server_disconnect()

  def play_podcast_url(self,podcast,url):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.add(url)
      self.mpd_client.play(0)
      self.server_disconnect()

      self.loaded = 'podcast-url'
      self.state = 'play'
      self.podcast = podcast
      self.player_img = '/static/images/playlists/' + podcast.image

  def outputs(self):
    output_list = []
    
    if (self.server_type == 'MPD'):
      self.server_connect()
      output_list = self.mpd_client.outputs()
      self.server_disconnect()
      
      names = []
      for output in output_list:
        names.append(output['outputname'])

    return output_list

  def toggle_output(self,id):
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.toggleoutput(id)
      self.server_disconnect()

################################################################################################################################################################
# CXN Control
################################################################################################################################################################

  def cxn_play_preset(self, preset_id):

    URL = 'http://' + self.server_name + ':' + self.server_port + '/' + CONFIG.CXN_ID + '/RecivaRadio/invoke'
    SOAPAction = '"urn:UuVol-com:service:UuVolControl:5#PlayPreset"'

    xml_body = """
    <u:PlayPreset xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <NewPresetNumberValue>""" +  str(preset_id) + """</NewPresetNumberValue>
    </u:PlayPreset>   
    """
    
    xml = """
    <?xml vesion="1.0" encoding="UTF-8"?>
      <s:Envelope 
        s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" 
        xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
      <s:Body>
    """ + xml_body + """
      </s:Body>
    </s:Envelope>
    """ 

    headers = { "Content-Type" : "text/xml", 
                "SOAPAction" : SOAPAction,
                "User-Agent" : "CambridgeConnect/3.2.1 (iOS) UPnP/1.0 DLNADOC/1.50 Platinum/1.0.4.11",
                "Host" : self.server_name}

    response = requests.post(URL, data=xml, headers=headers, verify=False)


  def cxn_play_remote(self,remote_key):

    URL = 'http://' + self.server_name + ':' + self.server_port + '/' + CONFIG.CXN_ID + '/RecivaSimpleRemote/invoke'
    SOAPAction = '"urn:UuVol-com:service:UuVolSimpleRemote:1#KeyPressed"'

    xml_body = """
    <u:KeyPressed xmlns:u="urn:UuVol-com:service:UuVolSimpleRemote:1">
      <Key>""" + remote_key + """</Key>
      <Duration>SHORT</Duration>
    </u:KeyPressed>   
    """
    
    xml = """
    <?xml vesion="1.0" encoding="UTF-8"?>
      <s:Envelope 
        s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" 
        xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
      <s:Body>
    """ + xml_body + """
      </s:Body>
    </s:Envelope>
    """
    
    headers = { "Content-Type" : "text/xml", 
                "SOAPAction" : SOAPAction,
                "User-Agent" : "CambridgeConnect/3.2.1 (iOS) UPnP/1.0 DLNADOC/1.50 Platinum/1.0.4.11",
                "Host" : self.server_name}

    response = requests.post(URL, data=xml, headers=headers, verify=False)


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

