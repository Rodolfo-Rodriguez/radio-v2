
import os, sys

class Config:

	PROJECT_ROOT_DIR = '/home/pi/develop/radio-v3'

	PROJECT_DB_DIR = 'database'
	PROJECT_DB_FILENAME = 'radio.db'
	SQLITE_DATABASE_FILE = ''

	PROJECT_CSV_DIR = 'database/csv_data' 
  	CSV_RADIOS_TABLE_FILE = 'radios_table.csv'
  	CSV_PROGRAM_TABLE_FILE = 'program_table.csv'
  	CSV_ARTIST_TABLE_FILE = 'artist_table.csv'
  	CSV_PLAYLIST_TABLE_FILE = 'playlist_table.csv'
  	CSV_PODCAST_TABLE_FILE = 'podcast_table.csv'
  	CSV_RADIO_LINK_TABLE_FILE = 'radio_link_table.csv'
  	CSV_ARTIST_LINK_TABLE_FILE = 'artist_link_table.csv'
  	CSV_PODCAST_LINK_TABLE_FILE = 'podcast_link_table.csv'

	PROJECT_RADIOS_IMG_DIR = 'app/static/images/radios'
	PROJECT_ARTIST_IMG_DIR = 'app/static/images/artist'
	PROJECT_ALBUM_IMG_DIR = 'app/static/images/albums'

	PLAYLIST_DIR = '/Playlists'
	PODCAST_FEED_FILE = '.podcast_feed.rss'
	DOWNLOADED_EPISODES_FILE = '.downloaded_episodes.txt'
	BASE_URI = 'USB/WD-500'

	DEFAULT_MPD_CLIENT = 'rune-1'
	DEFAULT_MPD_PORT = '6600'
	MPD_SERVERS = [ { "name":"Oficina", "server":"rune-1" } , { "name":"Sala", "server":"rune-2" } ]

	SOCIAL_SITES = ['twitter', 'instagram', 'youtube', 'spotify', 'apple', 'soundcloud']

	TIMEZONES = {'Uruguay':-3, 
				'Argentina':-3, 
				'Chile':-3, 
				'Spain':1, 
				'Brazil':-3, 
				'USA':-5, 
				'Peru':-5,
				'Australia':11, 
				'UK':0,
				'Italy':1,
				'Poland': 1,
				'Greece':2 }


	def __init__(self):

		self.SQLITE_DATABASE = "sqlite:///{}".format(os.path.join(self.PROJECT_ROOT_DIR, self.PROJECT_DB_DIR, self.PROJECT_DB_FILENAME))
