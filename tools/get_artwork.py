#!/usr/bin/python2

import os
import sys
import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File

if len(sys.argv) < 2:
  print '[ERROR] Uso: python ' + sys.argv[0] + ' <artist> <artist-path>'
  sys.exit(2)

artist_dir = sys.argv[1]
artist_path = sys.argv[2]

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
img_base_path = os.path.join(project_dir,'app/static/images/albums')

artist_img_path = os.path.join(img_base_path, artist_dir) 

os.mkdir(artist_img_path)

album_dir_list = os.listdir(artist_path)

skip_dirs = ['.DS_Store']

for album_dir in album_dir_list:

  if not(album_dir in skip_dirs):

    album_path = os.path.join(artist_path, album_dir)
    songs_list = os.listdir(album_path)
    
    song = songs_list[0]
    song_path = os.path.join(album_path, song)

    song_ext = song.split('.')[-1]

    if song_ext == 'm4a':
      
      audio = MP4(song_path)
      album = audio['\xa9alb']
      artist = audio['\xa9ART']
      cover = audio['covr']

      img_file = os.path.join(img_base_path, artist[0] + '/' + album[0] + '.png')

      open(img_file,'wb').write(cover[0])

      print album_dir + ' --> [MP4] ' + img_file

    else:

      print album_dir + ' --> [SKIP]'
