	
import os, sys
import urllib2
import xml.etree.cElementTree as ET
from BeautifulSoup import BeautifulSoup as BS
import wget
import eyed3
import datetime

from mpd import MPDClient

from flask import url_for

from .models import Podcast
from . import CONFIG, download_manager

MONTH_ABR = {
	'ene':'Jan',
	'feb':'Feb',
	'mar':'Mar',
	'abr':'Apr',
	'may':'May',
	'jun':'Jun',
	'jul':'Jul',
	'ago':'Aug',
	'sep':'Sep',
	'oct':'Oct',
	'nov':'Nov',
	'dic':'Dec'
}

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
	mpd_client = MPDClient()
	server_name = CONFIG.DEFAULT_SERVER_NAME
	server_port = CONFIG.DEFAULT_SERVER_PORT

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
#			item_pub_date = (item.find('pubDate').text).split(':')[0][0:-3]
			item_pub_date = (item.find('pubDate').text)
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

		self.mpd_client.connect(self.server_name, self.server_port)
		self.mpd_client.update(self.pod_uri)
		self.mpd_client.close()
		self.mpd_client.disconnect()

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
				
		if not(item_url in self.down_episodes):
			ep_file = item_url.split('/')[-1]
			if '.mp3' in ep_file:
				ep_file = ep_file.split('.mp3')[0] + '.mp3'
			pod_ep_name = self.podcast.pod_dir + '/' + ep_file

			download_manager.down_redirect_url = url_for('podcast.podcast_show', id=self.podcast.id)
			download_manager.download(item_url, pod_ep_name)

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

		down_ep_f = open(self.down_ep_file,'a')

		if not(url in self.down_episodes):
			ep_file = url.split('/')[-1]
			if '.mp3' in ep_file:
				ep_file = ep_file.split('.mp3')[0] + '.mp3'
			pod_ep_name = self.podcast.pod_dir + '/' + ep_file

			download_manager.down_redirect_url = url_for('podcast.podcast_show', id=self.podcast.id)
			download_manager.download(url, pod_ep_name)

			down_ep_f.write(url + '\n')
				
			## Re-Tag File

			if '.mp3' in ep_file:
				self.tag_file(pod_ep_name,title)

		down_ep_f.close()

		self.update_mpd_db()
		self.update_playlist()



	def add_episode_to_feed(self, title, url, pub_date):
		
		feed_filename = os.path.basename(self.podcast.feed_url)
		local_feed_file = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_FEED_DIR, feed_filename)

		image_filename = feed_filename.split('.')[0]
		
		tree = ET.parse(local_feed_file)
		root = tree.getroot()
		channel = root[0]
		items_list = channel.findall('item')

		pub_date_txt = datetime.datetime.now().strftime("%a %d %b %Y %H:%M:%S")

		feed_f = open(local_feed_file,'w')

		item_text = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{}</title>
    <link>https://www.the2rods.com</link>
    <image>
    	<url>http://feeds.the2rods.com/image/{}</url>
        <title>{}</title>
        <link>http://www.the2rods.com</link>
    </image>
    <description>{}</description>
    <pubDate>"{}"</pubDate>\n""".format(self.podcast.name, image_filename, self.podcast.name, self.podcast.description, pub_date_txt)

		feed_f.write(item_text)

		item_text = """
	<item>
		<title>{}</title>
		<pubDate>{}</pubDate>
		<description></description>
		<enclosure url="{}" length="0" type="audio/mpeg"/>
		<guid>{}</guid>
	</item>\n""".format(title, pub_date, url, url)

		feed_f.write(item_text)

		for item in items_list:
			item_url = item.find('enclosure').get('url')
			item_title = item.find('title').text
			item_pub_date = item.find('pubDate').text

			item_text = """
	<item>
		<title>{}</title>
		<pubDate>{}</pubDate>
		<description></description>
		<enclosure url="{}" length="0" type="audio/mpeg"/>
		<guid>{}</guid>
	</item>\n""".format(item_title, item_pub_date, item_url, item_url)

			feed_f.write(item_text)

		feed_f.write("\n</channel></rss>")

		feed_f.close()

		self.update_feed()

	def import_feed_from_web(self, url):

		feed_data = {}

		response = urllib2.urlopen(url)
		html = response.read()
		soup = BS(html)

		# Get Title

		title_tags = soup.findAll('title')

		if title_tags:
			feed_data['title'] = title_tags[0].string.split('|')[0]

		# Get Source

		source_tags = soup.findAll('source')
		if source_tags:
			feed_data['audio_url'] = source_tags[0]['src']

		# Get Date

		div_tags = soup.findAll('div')

		for tag in div_tags:
			if tag.attrs and ('class' in tag.attrs[0]):
				if tag['class'] == 'articulo--fecha':
					fecha_em = tag.contents[1].contents[0]


		pub_date_d = int(fecha_em.split(' ')[2])
		pub_date_mn = str(fecha_em.split(' ')[3]).lower()
		pub_date_y = int(fecha_em.split(' ')[4])

		pub_date_m = datetime.datetime.strptime(MONTH_ABR[pub_date_mn], '%b').month
		pub_date = datetime.date(pub_date_y, pub_date_m, pub_date_d)

		pub_date_wd = pub_date.strftime('%a')

		feed_data['pub_date'] = '{}, {} {} {} 12:00:00'.format(pub_date_wd, pub_date_d, MONTH_ABR[pub_date_mn], pub_date_y)

		return feed_data

	def upload_feed_to_server(self):

		feed_filename = os.path.basename(self.podcast.feed_url)
		upload_cmd = '/home/pi/bin/upload_feed.sh {}'.format(feed_filename)
		os.system(upload_cmd)

	def episode_url(self,track_num):
		
		self.update_items_list()

		item = self.items_list[int(track_num) - 1]
		
		item_url = item.find('enclosure').get('url')

		return item_url


	def episode_ext_url(self,track_num):

		pl_files = [line.rstrip('\n') for line in open(self.playlist_file)]
		filename = pl_files[track_num - 1].split('/')[-1]
		
		ep_ext_url = "http://192.168.1.203:8080/static{}/{}".format(self.podcast.pod_dir, filename)

		return ep_ext_url


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
