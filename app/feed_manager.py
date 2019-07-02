	
import os, sys
import urllib2
from BeautifulSoup import BeautifulSoup as BS
import datetime

####################################################################################
# Podcast Info
####################################################################################

class FeedManager:

	month_abr = {
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

	feed_url = ''

	title = ''
	audio_url = ''
	pubb_date = ''

	def __init__(self, url=''):

		self.feed_url = url
		self.source_url = url.split('/')[2]

		response = urllib2.urlopen(url)
		self.html = response.read()
		self.soup = BS(self.html)

	def get_title(self):
		
		if self.source_url in ['espectador.com', 'delsol.uy']:
			title_tags = self.soup.findAll('title')

			if title_tags:
				self.title = title_tags[0].string.split('|')[0]

		return self.title

	def get_audio_url(self):

		source_tags = self.soup.findAll('source')
		if source_tags:
			self.audio_url = source_tags[0]['src']
		else:
			self.audio_url = ''

		return self.audio_url

	def get_pub_date(self):

		if self.source_url in ['espectador.com']:
			div_tags = self.soup.findAll('div')

			for tag in div_tags:
				if tag.attrs and ('class' in tag.attrs[0]):
					if tag['class'] == 'articulo--fecha':
						fecha_em = tag.contents[1].contents[0]

			pub_date_d = int(fecha_em.split(' ')[2])
			pub_date_mn = str(fecha_em.split(' ')[3]).lower()
			pub_date_y = int(fecha_em.split(' ')[4])
			pub_date = datetime.date(pub_date_y, pub_date_m, pub_date_d)
			pub_date_m = datetime.datetime.strptime(self.month_abr[pub_date_mn], '%b').month


		if self.source_url in ['delsol.uy']:
			div_tags = self.soup.findAll('div')

			for tag in div_tags:
				if tag.attrs and ('class' in tag.attrs[0]):
					if tag['class'] == 'article-reproductor-box':
						fecha_em = tag.contents[1].findAll('span')[1].contents[0][0:10]

			pub_date_d = int(fecha_em.split('/')[0])
			pub_date_y = int(fecha_em.split('/')[2])
			pub_date_m = int(fecha_em.split('/')[1])
			pub_date = datetime.date(pub_date_y, pub_date_m, pub_date_d)
			pub_date_mn = pub_date.strftime('%b').lower()
			
		
		pub_date_wd = pub_date.strftime('%a')

		self.pub_date = '{}, {} {} {} 12:00:00'.format(pub_date_wd, pub_date_d, self.month_abr[pub_date_mn], pub_date_y)

		return self.pub_date
