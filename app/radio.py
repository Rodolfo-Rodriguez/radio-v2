import os, sys

from sqlalchemy import desc

from mpd import MPDClient

from .models import Radios,Artist,Playlist,Podcast
from . import CONFIG


################################################################################################################################################################
# Radio Player
################################################################################################################################################################

class RadioPlayer:
      mpd_client = CONFIG.DEFAULT_MPD_CLIENT
      mpd_port = CONFIG.DEFAULT_MPD_PORT
      mpd_servers = CONFIG.MPD_SERVERS
      client = MPDClient()
      fav_radios = []
      state = ''
      loaded = ''
      radio = Radios()
      playlist = Playlist()
      artist = Artist()
      podcast = Podcast()
      album = ''
      song_pos = 0
      player_img = ''
      playlist_len = 0

      def __init__(self):
          self.client = MPDClient()
          self.client.connect(self.mpd_client, self.mpd_port)
          self.state = 'stop'
          self.loaded = 'none'
          self.player_img = '/static/images/radios/empty.png'
          self.client.close()
          self.client.disconnect()
          #self.update_fav_radios()

      def connect(self,hostname):
          self.mpd_client = hostname
          self.client.disconnect()
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.disconnect()

      def disconnect(self):
          self.client.disconnect()

      def playradio(self,radio):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.clear()
          self.client.add(radio.url)
          self.client.play(0)
          self.playlist_len = int(self.client.status()['playlistlength'])
          self.client.close()
          self.client.disconnect()

          self.loaded = 'radio'
          self.state = 'play'
          self.radio = radio
          self.album = ''
          self.song_pos = 0
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
            if self.song_pos < (self.playlist_len - 1):
              self.client.connect(self.mpd_client, self.mpd_port)
              self.client.next()
              self.client.close()
              self.client.disconnect()
              self.song_pos = self.song_pos + 1

      def previous(self):
          if self.song_pos > 0:
            if self.loaded in ['album','playlist','podcast']:
              self.client.connect(self.mpd_client, self.mpd_port)
              self.client.previous()
              self.client.close()
              self.client.disconnect()
              self.song_pos = self.song_pos - 1

      def play_song(self,pos):
          self.client.connect(self.mpd_client, self.mpd_port)
          self.client.play(pos)
          self.client.close()
          self.client.disconnect()
          self.state = 'play'
          self.song_pos = int(pos)

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
              artist = playlist

            songs_list.append({'pos':pos,'title':title,'artist':artist,'track':pos+1,'time':time})
            pos = pos + 1

          self.client.close()
          self.client.disconnect()

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
          self.song_pos = 0
          self.player_img = '/static/images/playlists/' + playlist.image
          self.playlist_len = int(self.client.status()['playlistlength'])

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


      def artist_albums(self,artist):
          self.client.connect(self.mpd_client, self.mpd_port)

          album_list = self.client.list('album','artist',artist.name)

          album_info = []
          for album in album_list:
            alb_date = self.client.list('date','artist',artist.name,'album',album)
            album_info.append({'album':album,'date':alb_date})

          self.client.close()
          self.client.disconnect()

          album_info.sort(key=lambda x: x['date'])

          album_str =[]
          for alb_info in album_info:
              album_str.append(str(alb_info['album']))

          return album_str


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
              print song['file']

          self.client.play()

          self.loaded = 'album'
          self.state = 'play'
          self.artist = artist
          self.album = album
          self.song_pos = 0
          self.player_img = '/static/images/albums/' + str(artist.name) + '/' + str(album) + '.png'
          self.playlist_len = int(self.client.status()['playlistlength'])

          self.client.close()
          self.client.disconnect()

          return songs_list


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


      def load_podcast(self,podcast):
          self.client.connect(self.mpd_client, self.mpd_port)

          self.client.clear()
          self.client.load(podcast.playlist)
          self.client.play()

          self.loaded = 'podcast'
          self.state = 'play'
          self.podcast = podcast
          self.song_pos = 0
          self.player_img = '/static/images/playlists/' + podcast.image
          self.playlist_len = int(self.client.status()['playlistlength'])

          self.client.close()
          self.client.disconnect()

      def update_fav_radios(self):
          radio_list = Radios.query.order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).filter_by(fav=True).all()

          self.fav_radios = []

          for radio in radio_list:
            self.fav_radios.append(radio)







