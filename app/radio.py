import os
import time

from mpd import MPDClient
from cxn_client import CXNClient

from .models import Radios,Program,Artist,Playlist,Podcast, Bookmark, Preset, Episode
from .program_info import ProgramsInfo
from . import CONFIG


################################################################################################################################################################
# Radio Player
################################################################################################################################################################

class RadioPlayer:
  server_name = ''
  server_port = 0
  server_type = ''

  mpd_client = None
  cxn_client = None

  server_names = CONFIG.SERVER_NAMES
      
  bookmark_list = []
  bookmark_max = CONFIG.BOOKMARK_MAX

  state = ''
  loaded = ''  # none, radio, cxn_radio, podcast, playlist, album
  album = ''
  player_img = ''

  preset_playing = 0

  radio = None
  playlist = None
  artist = None
  podcast = None
  episode = None

  def __init__(self):
    self.state = 'stop'
    self.loaded = 'none'
    self.player_img = '{}/radios/empty.png'.format(CONFIG.FLASK_IMG_DIR)
    
    self.server_name = CONFIG.DEFAULT_SERVER_NAME
    self.server_port = CONFIG.DEFAULT_SERVER_PORT
    self.server_type = CONFIG.DEFAULT_SERVER_TYPE
    
    self.mpd_client = MPDClient()
    self.cxn_client = CXNClient(self.server_name, self.server_port, CONFIG.CXN_ID)
    #self.update_bookmarks()

################################################################################################################################################################
# Server - Connect / Disconnect
################################################################################################################################################################

  def select_server(self,hostname):
    self.server_name = hostname
    self.server_port = CONFIG.SERVER_PORTS[hostname]
    self._update_server_type(hostname)
    if self.server_type == 'CXN':
      self.cxn_client.update_server(self.server_name, self.server_port, CONFIG.CXN_ID)
    
    self.update_server_status()

  def server_connect(self):
    if self.server_type == 'MPD':
      self.mpd_client.connect(self.server_name, self.server_port)

  def server_disconnect(self):
    if self.server_type == 'MPD':
      self.mpd_client.disconnect()

  def current_server(self):
    return self.server_names[self.server_name]

  
################################################################################################################################################################
# Server - Status
################################################################################################################################################################

  def update_server_status(self):
    
    if self.server_type == 'CXN':
      
      self.cxn_client.update_playback_details()

      if self.cxn_client.playback_details['state'] == 'Playing':
        self.state = 'play'
        self.loaded = 'cxn_radio'
        self.player_img = self.cxn_client.playback_details['album-art-url']
        self._update_preset_playing()        
      else:
        self.state = 'stop'
        self.loaded = 'none'
        self.player_img = '{}/radios/empty.png'.format(CONFIG.FLASK_IMG_DIR)
    
    else:

      self.state = self.server_status('state')
      file = self.server_currentsong('file')
      
      if CONFIG.BASE_URI in file:
        if self.episode != None:
          self._set_loaded('episode', self.episode)
        else:
          self.loaded = 'none'
          self.player_img = '{}/radios/empty.png'.format(CONFIG.FLASK_IMG_DIR)
      else:
        self._update_radio_playing()
        if self.radio != None:
          self._set_loaded('radio', self.radio)
        else:
          if self.episode != None:
            self._set_loaded('episode-url', self.episode)
          else:
            self._set_loaded('podcast-url', self.podcast)

    self.update_bookmarks()


  def _update_server_type(self,hostname):
    if hostname in CONFIG.MPD_SERVERS:
      self.server_type = 'MPD'
    else:
      self.server_type = 'CXN'

  def _update_preset_playing(self):
    stream_url = self.cxn_client.playback_details['url']
    preset_url_list = [ preset.url for preset in Preset.query.all() ]
    if stream_url in preset_url_list: 
      self.preset_playing = preset_url_list.index(stream_url) + 1
    else:
      self.preset_playing = 0

  def _update_radio_playing(self):
    stream_url = self.server_currentsong('file')
    radio_url_list = [ radio.url for radio in Radios.query.order_by(Radios.id).all() ]
    if stream_url in radio_url_list: 
      radio_id = radio_url_list.index(stream_url) + 1
      self.radio = Radios.query.filter_by(id=radio_id).first()

  def update_bookmarks(self):
    self.bookmark_list = Bookmark.query.order_by(Bookmark.priority).all()[0:self.bookmark_max]


  def power_state(self):
    if (self.server_type == 'CXN'):
      power_state = self.cxn_client.get_power_state()
    else:
      power_state = 'Unknown'

    return power_state


  def _set_loaded(self, loaded, loaded_obj, state='play'):

    if loaded == 'radio':
      self.loaded = 'radio'
      self.state = state
      self.radio = loaded_obj
      self.playlist = None
      self.artist = None
      self.podcast = None
      self.episode = None
      self.player_img = os.path.join(CONFIG.FLASK_IMG_DIR, 'radios', self.radio.image)
    
    elif loaded == 'playlist':
      self.loaded = 'playlist'
      self.state = state
      self.radio = None
      self.playlist = loaded_obj
      self.artist = None
      self.podcast = None
      self.episode = None

    elif loaded == 'artist':
      self.loaded = 'artist'
      self.state = state
      self.radio = None
      self.playlist = None
      self.artist = loaded_obj
      self.podcast = None
      self.episode = None

    elif loaded == 'podcast-url':
      self.loaded = 'podcast-url'
      self.state = state
      self.radio = None
      self.playlist = None
      self.artist = None
      self.podcast = loaded_obj
      self.episode = None
      self.player_img = os.path.join(CONFIG.FLASK_IMG_DIR, 'playlists', self.podcast.image)

    elif loaded == 'episode':
      self.loaded = 'episode'
      self.state = state
      self.radio = None
      self.playlist = None
      self.artist = None
      self.podcast = None
      self.episode = loaded_obj
      self.player_img = os.path.join(CONFIG.FLASK_IMG_DIR, 'playlists', self.episode.podcast.image)

    elif loaded == 'episode-url':
      self.loaded = 'episode'
      self.state = state
      self.radio = None
      self.playlist = None
      self.artist = None
      self.podcast = None
      self.episode = loaded_obj
      self.player_img = os.path.join(CONFIG.FLASK_IMG_DIR, 'playlists', self.episode.podcast.image)

################################################################################################################################################################
# Player Control
################################################################################################################################################################

  def power(self):
    if (self.server_type == 'CXN'):
      power_state = self.cxn_client.get_power_state()
      if power_state == 'ON':
        self.cxn_client.send_command('POWER_OFF')
      else:
        self.cxn_client.send_command('POWER_ON')
      
      self.cxn_client.press_remote_key('POWER','SHORT')

  def vol_up(self):
    if (self.server_type == 'CXN'):
      self.cxn_client.send_command('VOL_UP')
    else:
      self.server_connect()
      vol = int(self.mpd_client.status()['volume'])
      if vol < 100:
        self.mpd_client.setvol(vol + 1)
      self.server_disconnect()


  def vol_down(self):
    if (self.server_type == 'CXN'):
      self.cxn_client.send_command('VOL_DOWN')
    else:
      self.server_connect()
      vol = int(self.mpd_client.status()['volume'])
      if vol > 0:
        self.mpd_client.setvol(vol - 1)
      self.server_disconnect()

  def vol_mute(self):
    if (self.server_type == 'CXN'):
      self.cxn_client.press_remote_key('MUTE','SHORT')
    else:
      self.server_connect()
      vol = int(self.mpd_client.status()['volume'])
      if vol > 0:
        self.mpd_client.setvol(0)
      else:
        self.mpd_client.setvol(CONFIG.DEFAULT_VOLUME  )
      self.server_disconnect()

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

    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.add(radio.url)
      self.mpd_client.play(0)
      self.server_disconnect()

      self.loaded = 'radio'
      self.state = 'play'
      self.radio = radio
      self.album = ''
      self.player_img = os.path.join(CONFIG.FLASK_IMG_DIR, 'radios', radio.image)

      self.preset_playing = radio.preset_number()

    else:
      if (radio.preset > 0) and (radio.preset < 21):
        self.cxn_client.play_preset(radio.preset)
        time.sleep(4)
        self.update_server_status()
        
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
# CXN Control
################################################################################################################################################################

  #--> Press Remote Key
  def cxn_press_remote_key(self, key, duration):

    self.cxn_client.press_remote_key(key, duration)

  #--> Play Preset
  def cxn_play_preset(self, preset_id):
    
    self.cxn_client.play_preset(preset_id)
    self.loaded = 'cxn_radio'
    self.preset_playing = int(preset_id)

  #--> Play Radio ID
  def cxn_play_radio(self, radio_id):
    
    self.cxn_client.play_radio(radio_id)
    self.loaded = 'cxn_radio'
    self.preset_playing = 0
    self.station_id_playing = radio_id

  #--> Send Command
  def cxn_send_command(self, command):

    self.cxn_client.send_command(command)

  #--> Get Power State
  def cxn_get_power_state(self):

    state = self.cxn_client.get_power_state()
    return state

  def cxn_search_radio(self, name, location):

    radio_list = self.cxn_client.search_radio(name, location)
    return radio_list

  def cxn_locations(self):

    location_list = self.cxn_client.locations()
    return location_list

  def cxn_genre_list(self):

    genre_list = self.cxn_client.genre_list()
    return genre_list

  def list_radios_in_cxn_location(self, location_id):

    radio_list = self.cxn_client.list_radios_in_location(location_id)
    return radio_list

  def list_radios_in_cxn_genre(self, genre_id):

    radio_list = self.cxn_client.list_radios_in_genre(genre_id)
    return radio_list


  def cxn_set_preset(self, preset_id):

    self.cxn_client.set_preset(preset_id, self.station_id_playing)
    

################################################################################################################################################################
# Status
################################################################################################################################################################

  def play_pause(self):

    if (self.server_type == 'MPD'):
      self.server_connect()          
      
      if self.state == 'play':
        self.mpd_client.pause()
        self.state = 'pause'
      else:
        self.mpd_client.play()
        self.state = 'play'
      
      self.server_disconnect()
    else:
      self.cxn_client.press_remote_key('PLAY_PAUSE','SHORT')
      if self.state == 'play':
        self.state = 'pause'
      else:
        self.state = 'play'          
          
  def play(self):
    self.state = 'play'
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.play()
      self.server_disconnect()
    else:
      self.cxn_client.press_remote_key('PLAY_PAUSE','SHORT')

  def stop(self):
    self.state = 'stop'
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.stop()
      self.server_disconnect()
    else:
      self.cxn_client.press_remote_key('STOP','SHORT')

  def pause(self):
    self.state = 'pause'
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.pause()
      self.server_disconnect()
    else:
      self.cxn_client.press_remote_key('PLAY_PAUSE','SHORT')

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
        self.cxn_client.press_remote_key('SKIP_NEXT','SHORT')

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
        self.cxn_client.press_remote_key('SKIP_PREVIOUS','SHORT')

  def volume(self):
    if (self.server_type == 'MPD'):
      self.server_connect()
      volume = int(self.mpd_client.status()['volume'])
      self.server_disconnect()
    else:
      volume = CONFIG.DEFAULT_VOLUME

    return volume

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

      self._set_loaded('podcast-url', podcast)

  def play_episode_file(self, episode):

    url = CONFIG.BASE_URI + episode.podcast.pod_dir + '/' + episode.local_file

    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.add(url)
      self.mpd_client.play(0)
      self.server_disconnect()

      self._set_loaded('episode', episode)

  def play_episode_url(self, episode):

    url = episode.url
    if (self.server_type == 'MPD'):
      self.server_connect()
      self.mpd_client.clear()
      self.mpd_client.add(url)
      self.mpd_client.play(0)
      self.server_disconnect()

      self._set_loaded('episode-url', episode)

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
