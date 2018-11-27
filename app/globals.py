
import os, sys
import json

################################################################################################################################################################
# Variables Globales
################################################################################################################################################################

class GlobalValues:

	project_root_dir = '/home/pi/develop/radio-v2'
	config_file = 'config/config.json'

	database_file = ''

	artist_images_dir = ''
	albums_images_dir = ''

	default_mpd_client = ''
	default_mpd_port = ''
	mpd_servers = ''

	podcast_feed_file = ''
	downloaded_episodes_file = ''
	playlist_dir = ''
	base_uri = ''

  	csv_radios_table_file = ''
  	csv_artist_table_file = ''
  	csv_playlist_table_file = ''
  	csv_podcast_table_file = ''

	def __init__(self):

		self.read_config_file()

		self.database_file = "sqlite:///{}".format(os.path.join(self.project_root_dir, self.project_db_dir, self.project_db_filename))


	def read_config_file(self):

		config_file_path = os.path.join(self.project_root_dir, self.config_file)

		f_conf = open(config_file_path,'r')
		input_data = json.load(f_conf)
		f_conf.close()

		self.project_db_dir = input_data['project_db_dir']
		self.project_db_filename = input_data['project_db_filename']

		self.project_csv_dir = input_data['project_csv_dir']
  		self.csv_radios_table_file = input_data['csv_radios_table_file']
  		self.csv_artist_table_file = input_data['csv_artist_table_file']
  		self.csv_playlist_table_file = input_data['csv_playlist_table_file']
  		self.csv_podcast_table_file = input_data['csv_podcast_table_file']

		self.default_mpd_client = input_data['default_mpd_client']
		self.default_mpd_port = input_data['default_mpd_port']
		self.mpd_servers = input_data['mpd_servers']
		
		self.artist_images_dir= os.path.join(self.project_root_dir, input_data['artist_images_dir'])
		self.albums_images_dir= os.path.join(self.project_root_dir, input_data['albums_images_dir'])

		self.podcast_feed_file = input_data['podcast_feed_file']
		self.downloaded_episodes_file = input_data['downloaded_episodes_file']
		self.playlist_dir = input_data['playlist_dir']
		self.base_uri = input_data['base_uri']

