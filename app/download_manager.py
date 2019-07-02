	
import urllib2

####################################################################################
# Download Manager
####################################################################################

class DownloadManager:
	down_in_prog = 0
	down_redirect_url = ''
	down_url = ''
	down_file = ''
	down_file_size = 0
	down_curr_file_size = 0
	down_prog_bar = 0.0
	down_prog_bar_txt = ''

	def __init__(self):
		self.down_in_prog = 0

	def download(self, url, filename):
		self.down_url = url
		self.down_file = filename

		self.init_prog_bar()

		u = urllib2.urlopen(url)
		meta = u.info()
		self.down_file_size = int(meta.getheaders("Content-Length")[0])

		f = open(filename, 'wb')

		self.down_curr_file_size = 0
		self.down_in_prog = 1
		block_sz = 8192

		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break
				
			f.write(buffer)

			self.down_curr_file_size = self.down_curr_file_size + len(buffer)
			self.update_prog_bar()

		self.down_in_prog = 0

		self.stop_prog_bar()

	def init_prog_bar(self):
		self.down_prog_bar = 0
		self.down_prog_bar_txt = 'Getting info for -> {}'.format(self.down_url)

	def stop_prog_bar(self):
		self.down_prog_bar = 1
		self.down_prog_bar_txt = '{} [ {:.0f} MB ]'.format(self.down_file, float(self.down_file_size) / 1000 / 1000)

	def update_prog_bar(self):
		self.down_prog_bar = float(self.down_curr_file_size) / float(self.down_file_size)	
		self.down_prog_bar_txt = 'Downloading -> {} [ {:.0f} MB / {:.0f} MB ]'.format(self.down_file, float(self.down_curr_file_size) / 1000 / 1000, float(self.down_file_size) / 1000 / 1000)

		








