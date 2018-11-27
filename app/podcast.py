
import os, sys
import xml.etree.ElementTree as ET
import wget
import eyed3

from mpd import MPDClient

from .models import Podcast
from . import global_values 

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
	mpd_client = global_values.default_mpd_client
	mpd_port = global_values.default_mpd_port

	def __init__(self,podcast):
		self.podcast = podcast
		self.feed_file = podcast.pod_dir + '/' + global_values.podcast_feed_file
		self.down_ep_file = podcast.pod_dir + '/' + global_values.downloaded_episodes_file
		self.playlist_file = global_values.playlist_dir + '/' + podcast.playlist + '.m3u'
		self.pod_uri = global_values.base_uri + podcast.pod_dir

	def update_items_list(self):

		if os.path.isfile(self.feed_file):
			os.remove(self.feed_file)
		
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
			item_pub_date = item.find('pubDate').text
			item_url = item.find('enclosure').get('url')

			if (item_url in self.down_episodes):
				item_down = 'Yes'
			else:
				item_down = 'No'

			if (self.podcast.feed_filter in item_url):
				episodes_list.append({'track':track_num,'title':item_title,'pubdate':item_pub_date,'downloaded':item_down, 'url':item_url})
			
			track_num = track_num + 1

		return episodes_list

	def update_mpd_db(self):

		self.client.connect(self.mpd_client, self.mpd_port)
		self.client.update(self.pod_uri)
		self.client.close()
		self.client.disconnect()

	def update_playlist(self):

		inc_files = [f for f in os.listdir(self.podcast.pod_dir) if '.mp3' in f]

		inc_files.sort(reverse=True)

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
		
		if not(item_url in self.down_episodes):
			ep_file = item_url.split('/')[-1]
			if '.mp3' in ep_file:
				ep_file = ep_file.split('.mp3')[0] + '.mp3'
			pod_ep_name = self.podcast.pod_dir + '/' + ep_file
			wget.download(item_url, pod_ep_name)
			down_ep_f.write(item_url + '\n')

			## Tag File

			pub_date = item_pub_date.split(':')[0]
			pub_date = pub_date[0:-3]
			title_tag = pub_date + ' - ' + item_title

			if '.mp3' in ep_file:
				self.tag_file(pod_ep_name,title_tag)
				
		down_ep_f.close()

		self.update_mpd_db()
		self.update_playlist()



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




