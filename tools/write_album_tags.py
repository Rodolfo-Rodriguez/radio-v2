#!/usr/bin/python2

# This Python file uses the following encoding: utf-8

import os
import sys
import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

if len(sys.argv) < 3:
  print '[ERROR] Uso: python ' + sys.argv[0] + ' <album-path> <album-tag>'
  sys.exit(2)

album_path = sys.argv[1]

album_tag = sys.argv[2]

songs_list = os.listdir(album_path)
    
for song in songs_list:
  song_path = os.path.join(album_path, song)

  song_ext = song.split('.')[-1]

  if song_ext == 'm4a':
    audio = MP4(song_path)

    audio['\xa9alb'] = unicode(album_tag,'utf-8')

    audio.save()

    print album_path + ' --> [MP4] Album: ' + album_tag 

  elif song_ext == 'mp3':
    audio = EasyID3(song_path)

    audio['album'] = unicode(album_tag,'utf-8')

    audio.save()

    print album_path + ' --> [MP3] Album: ' + album_tag 
