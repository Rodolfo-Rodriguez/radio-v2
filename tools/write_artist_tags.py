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
  print '[ERROR] Uso: python ' + sys.argv[0] + ' <album-path> <artist-tag>'
  sys.exit(2)

album_path = sys.argv[1]

artist_tag = sys.argv[2]

songs_list = os.listdir(album_path)
    
for song in songs_list:
  song_path = os.path.join(album_path, song)

  song_ext = song.split('.')[-1]

  if song_ext == 'm4a':
    audio = MP4(song_path)

    audio['\xa9ART'] = unicode(artist_tag,'utf-8')

    audio.save()

    print album_path + ' --> [MP4] Artist: ' + artist_tag 

  elif song_ext == 'mp3':
    audio = EasyID3(song_path)

    audio['artist'] = unicode(artist_tag,'utf-8')

    audio.save()

    print album_path + ' --> [MP3] Artist: ' + artist_tag 
