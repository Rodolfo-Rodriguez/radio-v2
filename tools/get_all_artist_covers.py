#!/usr/bin/python2

import sys, os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(base_path)

from app import CONFIG

import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File


if len(sys.argv) < 2:
  print '[ERROR] Uso: ' + sys.argv[0] + ' [artist_dir]'
  sys.exit(2)


skip_dirs = ['.AppleDouble']

artist_dir = sys.argv[1]

dest_dir = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_ALBUMS_IMG_DIR)

audio_files = []

for root, dirs, files in os.walk(artist_dir):
	for filename in files:
		if filename.startswith('01'):
			audio_files.append(os.path.join(root, filename))


for file in audio_files:

	audio = File(file)
	artwork_find = False 

	if file.endswith('m4a'):
		
		artist = audio['\xa9ART'][0]
		album = audio['\xa9alb'][0]
		
		if 'covr' in audio:
			artwork = audio['covr'][0]
			artwork_find = True

		cover_filename = os.path.join(dest_dir, artist, album + '.png')
		print '[MP4] --> ' + artist + '/' + album + '.png'

	elif file.endswith('mp3'):
		
		artist = audio['TPE1']
		album = audio['TALB']
		artwork = audio['APIC:'].data
		artwork_find = True

		cover_filename = os.path.join(dest_dir, str(artist), str(album) + '.png')
		print '[MP3] --> ' + str(artist) + '/' + str(album) + '.png'
	
	
	album_dir = os.path.join(dest_dir, str(artist))
	if not(os.path.exists(album_dir)):
		os.mkdir(album_dir)
        
        if artwork_find:
		open(cover_filename,'wb').write(artwork)

