	
import os, sys
import urllib2
#import xml.etree.ElementTree as ET
import xml.etree.cElementTree as ET
import wget
import eyed3
import datetime

from mpd import MPDClient

from flask import url_for

from .models import Podcast
from . import CONFIG

####################################################################################
# Podcast Info
####################################################################################

class PodcastInfo:
	feed_file = ''
	down_ep_file = ''
	playlist_file = ''
	podcast = Podcast()
	items_list = []
	down_episodes = []
	pod_uri = ''
	client = MPDClient()
	mpd_client = CONFIG.DEFAULT_SERVER_NAME
	mpd_port = CONFIG.DEFAULT_SERVER_PORT

	def __init__(self,podcast):
		self.podcast = podcast
		self.feed_file = os.path.join(podcast.pod_dir, CONFIG.PODCAST_FEED_FILE)
		self.down_ep_file = os.path.join(podcast.pod_dir, CONFIG.DOWNLOADED_EPISODES_FILE)
		self.playlist_file = os.path.join(CONFIG.PLAYLIST_DIR, podcast.playlist + '.m3u')
		self.pod_uri = CONFIG.BASE_URI + podcast.pod_dir

	def update_feed(self):

		if os.path.isfile(self.feed_file):
			os.remove(self.feed_file)
		
		wget.download(self.podcast.feed_url, self.feed_file)    	


	def update_items_list(self):

		if not(os.path.isfile(self.feed_file)):		
			wget.download(self.podcast.feed_url, self.feed_file)    	

		tree = ET.parse(self.feed_file)
		root = tree.getroot()
		channel = root[0]
		self.items_list = channel.findall('item')


	def episode_list(self):

		episodes_list = []
		track_num = 1
		self.down_episodes = [line.rstrip('\n') for line in open(self.down_ep_file)]

		for item in self.items_list:
			item_title = item.find('title').text
			item_pub_date = (item.find('pubDate').text).split(':')[0][0:-3]
			item_url = item.find('enclosure').get('url')
			item_length = str(int(item.find('enclosure').get('length')) / 1000 / 1000) + ' MB'

			item_desc = item.find('description').text

			if item_desc:
				if '<p>' in item_desc:
					item_desc = item_desc.split('<p>')[1].split('</p>')[0]
			else:
				item_desc = ''

			if (item_url in self.down_episodes):
				item_down = 'Yes'
			else:
				item_down = 'No'

			feed_filter_list = self.podcast.feed_filter.split(',')

			ep_included = False
			for feed_filter in feed_filter_list:
				if (feed_filter in item_url) and not(ep_included):
					episodes_list.append({'track':track_num,'title':item_title,'description':item_desc,'pubdate':item_pub_date,'downloaded':item_down, 'url':item_url, 'length':item_length})
					ep_included = True
			
			track_num = track_num + 1

		return episodes_list

	def update_mpd_db(self):

		self.client.connect(self.mpd_client, self.mpd_port)
		self.client.update(self.pod_uri)
		self.client.close()
		self.client.disconnect()

	def update_playlist(self):

		inc_files = [f for f in os.listdir(self.podcast.pod_dir) if '.mp3' in f]

		inc_files.sort(reverse=False)

		pl_f = open(self.playlist_file,'w')

		for f in inc_files:
  			f_uri = self.pod_uri + '/' + f
  			pl_f.write(f_uri + '\n')

		pl_f.close()

	def remove_from_downloaded(self,ep_filename):

		self.down_episodes = [line.rstrip('\n') for line in open(self.down_ep_file)]

		down_ep_f = open(self.down_ep_file,'w')

		for ep_url in self.down_episodes:
			if not(ep_filename in ep_url):
				down_ep_f.write(ep_url + '\n')

		down_ep_f.close()


	def tag_file(self,file_name,title_tag):

		audio = eyed3.load(file_name)
		audio.initTag()
		audio.tag.title = unicode(title_tag)
		audio.tag.artist = unicode(self.podcast.name)
		audio.tag.save()

	def file_tags(self,track_num):

		pl_files = [line.rstrip('\n') for line in open(self.playlist_file)]
		file_name = pl_files[track_num - 1].split('/')[-1]
		audio_file = self.podcast.pod_dir + '/' + file_name
		audio = eyed3.load(audio_file)
		title = audio.tag.title
		artist = audio.tag.artist

		return [title, artist]


	def write_file_tags(self,track_num,title_tag):

		pl_files = [line.rstrip('\n') for line in open(self.playlist_file)]
		file_name = pl_files[track_num - 1].split('/')[-1]
		audio_file = self.podcast.pod_dir + '/' + file_name
		audio = eyed3.load(audio_file)

		audio.initTag()
		audio.tag.title = unicode(title_tag)
		audio.tag.album = unicode(self.podcast.name)
		audio.tag.artist = unicode(self.podcast.name)
		audio.tag.save()

		self.update_mpd_db()

	
	def download_episode(self,track_num):
		
		self.down_episodes = [line.rstrip('\n') for line in open(self.down_ep_file)]
		self.update_items_list()

		down_ep_f = open(self.down_ep_file,'a')

		item = self.items_list[int(track_num) - 1]
		
		item_url = item.find('enclosure').get('url')
		item_title = item.find('title').text
		item_pub_date = item.find('pubDate').text

		CONFIG.DOWN_URL = item_url
		CONFIG.DOWN_REDIRECT_URL = url_for('podcast.podcast_show', id=self.podcast.id)

		u = urllib2.urlopen(item_url)
		meta = u.info()
		CONFIG.DOWN_FILE_SIZE = int(meta.getheaders("Content-Length")[0])
		
		if not(item_url in self.down_episodes):
			ep_file = item_url.split('/')[-1]
			if '.mp3' in ep_file:
				ep_file = ep_file.split('.mp3')[0] + '.mp3'
			pod_ep_name = self.podcast.pod_dir + '/' + ep_file

			CONFIG.DOWN_FILE = pod_ep_name

			f = open(pod_ep_name, 'wb')

			CONFIG.DOWN_CURR_FILE_SIZE = 0
			CONFIG.DOWN_IN_PROG = 1
			block_sz = 8192

			while True:
				buffer = u.read(block_sz)
				if not buffer:
					break
				
				f.write(buffer)

				CONFIG.DOWN_CURR_FILE_SIZE += len(buffer)
				CONFIG.DOWN_PROG_BAR = float(CONFIG.DOWN_CURR_FILE_SIZE) / float(CONFIG.DOWN_FILE_SIZE)

			CONFIG.DOWN_IN_PROG = 0

			down_ep_f.write(item_url + '\n')

			## Re-Tag File

			if self.podcast.retag:				
				pub_date_d = int(item_pub_date.split(' ')[1])
				pub_date_mn = item_pub_date.split(' ')[2]
				pub_date_y = int(item_pub_date.split(' ')[3])

				pub_date_m = datetime.datetime.strptime(pub_date_mn, '%b').month

				pub_date = datetime.date(pub_date_y, pub_date_m, pub_date_d)
				pub_date_txt = pub_date.strftime('%Y.%m.%d')

				title_tag = pub_date_txt + ' - ' + item_title
			else:
				title_tag = item_title

			if '.mp3' in ep_file:
				self.tag_file(pod_ep_name,title_tag)
				
		down_ep_f.close()

		self.update_mpd_db()
		self.update_playlist()


	def download_episode_from_url(self,url,title):
		
		self.down_episodes = [line.rstrip('\n') for line in open(self.down_ep_file)]
		self.update_items_list()

		CONFIG.DOWN_URL = url
		CONFIG.DOWN_REDIRECT_URL = url_for('podcast.podcast_show', id=self.podcast.id)

		u = urllib2.urlopen(url)
		meta = u.info()
		CONFIG.DOWN_FILE_SIZE = int(meta.getheaders("Content-Length")[0])

		down_ep_f = open(self.down_ep_file,'a')

		if not(url in self.down_episodes):
			ep_file = url.split('/')[-1]
			if '.mp3' in ep_file:
				ep_file = ep_file.split('.mp3')[0] + '.mp3'
			pod_ep_name = self.podcast.pod_dir + '/' + ep_file

			CONFIG.DOWN_FILE = pod_ep_name

			f = open(pod_ep_name, 'wb')

			CONFIG.DOWN_CURR_FILE_SIZE = 0
			CONFIG.DOWN_IN_PROG = 1
			block_sz = 8192

			while True:
				buffer = u.read(block_sz)
				if not buffer:
					break
				
				f.write(buffer)

				CONFIG.DOWN_CURR_FILE_SIZE += len(buffer)
				CONFIG.DOWN_PROG_BAR = float(CONFIG.DOWN_CURR_FILE_SIZE) / float(CONFIG.DOWN_FILE_SIZE)


			CONFIG.DOWN_IN_PROG = 0

			down_ep_f.write(url + '\n')
				

			## Re-Tag File

			if '.mp3' in ep_file:
				self.tag_file(pod_ep_name,title)

		down_ep_f.close()

		self.update_mpd_db()
		self.update_playlist()

	def episode_url(self,track_num):
		
		self.update_items_list()

		item = self.items_list[int(track_num) - 1]
		
		item_url = item.find('enclosure').get('url')

		return item_url


	def create_init_files(self):

		if not(os.path.exists(self.podcast.pod_dir)):
			os.mkdir(self.podcast.pod_dir)
			
			with open(self.down_ep_file, 'a'):
				os.utime(self.down_ep_file, None)

			if not(os.path.exists(self.playlist_file)):
				with open(self.playlist_file, 'a'):
					os.utime(self.playlist_file, None)

	
	def delete_episode(self,track_num):

		pl_files = [line.rstrip('\n') for line in open(self.playlist_file)]
		filename = pl_files[track_num - 1].split('/')[-1]
		ep_file = self.podcast.pod_dir + '/' + filename

		os.remove(ep_file)

		self.update_mpd_db()
		self.update_playlist()
		self.remove_from_downloaded(filename)




