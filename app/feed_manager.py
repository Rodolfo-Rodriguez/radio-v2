
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
	pub_date = ''
	description = ''

	def __init__(self, url=''):

		self.feed_url = url
		self.source_url = url.split('/')[2]

		response = urllib2.urlopen(url)
		self.html = response.read()
		self.soup = BS(self.html)

	def get_title(self):
		
		if self.source_url == 'espectador.com':
			title_tags = self.soup.findAll('title')

			if title_tags:
				self.title = title_tags[0].string.split('|')[0]

		if self.source_url == 'delsol.uy':
			h2_tags = self.soup.findAll('h2')
			for tag in h2_tags:
				if tag['class'] == 'articulo-titulo':
					a_tag = tag.findAll('a')
					self.title = a_tag[0]['title']

		if self.source_url == 'www.oceano.uy':
			h1_tags = self.soup.findAll('h1')
			for tag in h1_tags:
				print tag.string
				if tag['class'] == 'ng-binding':
					self.title = tag.string

		return self.title

	def get_audio_url(self):

		self.audio_url = ''

		if self.source_url == 'espectador.com':
		
			source_tags = self.soup.findAll('source')
			if source_tags:
				self.audio_url = source_tags[0]['src']

		if self.source_url == 'delsol.uy':
		
			div_tags = self.soup.findAll('div')
			for tag in div_tags:
				if tag.attrs and ('class' in tag.attrs[0]):
					if tag['class'] == 'articulo-audio':
						self.audio_url = tag.findAll('audio')[0]['src']

		if self.source_url == 'www.oceano.uy':
			self.audio_url = ''

		return self.audio_url

	def get_pub_date(self):

		if self.source_url == 'espectador.com':
			div_tags = self.soup.findAll('div')

			for tag in div_tags:
				if tag.attrs and ('class' in tag.attrs[0]):
					if tag['class'] == 'articulo--fecha':
						fecha_em = tag.contents[1].contents[0]

			pub_date_d = int(fecha_em.split(' ')[2])
			pub_date_mn = self.month_abr[str(fecha_em.split(' ')[3]).lower()]
			pub_date_y = int(fecha_em.split(' ')[4])
			pub_date_m = datetime.datetime.strptime(pub_date_mn, '%b').month

		if self.source_url == 'delsol.uy':
			div_tags = self.soup.findAll('div')

			for tag in div_tags:
				if tag.attrs and ('class' in tag.attrs[0]):
					if tag['class'] == 'articulo-categoria-fecha':
						fecha_em = tag.findAll('small')[0].contents[0]

			pub_date_d = int(fecha_em.split(' ')[1])
			pub_date_y = 2019
			pub_date_mn = self.month_abr[str(fecha_em.split(' ')[3])[0:3].lower()]
			pub_date_m = datetime.datetime.strptime(pub_date_mn, '%b').month			
		
		if self.source_url == 'www.oceano.uy':
			pub_date_d = 1
			pub_date_y = 2019
			pub_date_m = 1			

		pub_date = datetime.date(pub_date_y, pub_date_m, pub_date_d)
		
		self.pub_date = '{}.{}.{}-12:00:00'.format( pub_date.strftime('%Y'), pub_date.strftime('%m'), pub_date.strftime('%d') )

		return self.pub_date

	
	def get_description(self):

		if self.source_url == 'espectador.com':
			h4_tags = self.soup.findAll('h4')

			if h4_tags:
				self.description = h4_tags[0].string

		if self.source_url == 'delsol.uy':
			self.description = ''

		if self.source_url == 'www.oceano.uy':
			self.description = ''

		return self.description

