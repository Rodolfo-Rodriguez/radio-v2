
import os, sys

class Config:

	PROJECT_ROOT_DIR = '/home/pi/develop/radio-v3'

	PROJECT_DB_DIR = 'database'
	PROJECT_DB_FILENAME = 'radio.db'
	SQLITE_DATABASE_FILE = ''

	PROJECT_CSV_DIR = 'database/csv_data'

	CSV_TABLE_FILE = {
		'Radios' : 'radios_table.csv',
		'Program' : 'program_table.csv',
		'Artist' : 'artist_table.csv',
		'Playlist' : 'playlist_table.csv',
		'Podcast' : 'podcast_table.csv',
		'Radio_Link' : 'radio_link_table.csv',
		'Artist_Link' : 'artist_link_table.csv',
		'Podcast_Link' : 'podcast_link_table.csv',
		'Bookmark' : 'bookmark_table.csv',
		'Preset' : 'preset_table.csv'
	}

	FLASK_IMG_DIR = '/static/images'

	PROJECT_RADIOS_IMG_DIR = 'app/static/images/radios'
	PROJECT_ARTIST_IMG_DIR = 'app/static/images/artist'
	PROJECT_ALBUM_IMG_DIR = 'app/static/images/albums'
	PROJECT_FEED_DIR = 'app/static/feeds'

	PODCAST_BASE_URL = '/static/Podcast'

	PLAYLIST_DIR = '/Playlists'
	PODCAST_FEED_FILE = '.podcast_feed.rss'
	DOWNLOADED_EPISODES_FILE = '.downloaded_episodes.txt'
	BASE_URI = 'USB/WD-500'

	DEFAULT_SERVER_NAME = 'rune-1'
	DEFAULT_SERVER_PORT = '6600'
	DEFAULT_SERVER_TYPE = 'MPD'
	
	MPD_SERVERS = ["rune-1", "rune-2"]

	SERVER_NAMES = { 
		"rune-1":"MPD-Office",
		"cxn":"CXN" 
	}
	
	SERVER_PORTS = { 
		"rune-1":"6600",
		"cxn":"8050"
	}
			
	CXN_ID = '9ffd0730-00fb-455b-aa2f-8fc8df0c268f'

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

	BOOKMARK_MAX = 10
	DEFAULT_VOLUME = 50

	def __init__(self):

		self.SQLITE_DATABASE = "sqlite:///{}".format(os.path.join(self.PROJECT_ROOT_DIR, self.PROJECT_DB_DIR, self.PROJECT_DB_FILENAME))
