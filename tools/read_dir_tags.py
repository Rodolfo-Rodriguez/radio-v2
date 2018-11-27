#!/usr/bin/python2

# This Python file uses the following encoding: utf-8

import os
import sys
import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

if len(sys.argv) < 2:
  print '[ERROR] Uso: python ' + sys.argv[0] + ' <album-path>'
  sys.exit(2)

album_path = sys.argv[1]

songs_list = os.listdir(album_path)
    
for song in songs_list:
  song_path = os.path.join(album_path, song)

  song_ext = song.split('.')[-1]

  if song_ext == 'm4a':
    audio = MP4(song_path)
    album = audio['\xa9alb']
    artist = audio['\xa9ART']
    track = audio['\xa9nam']

    print album_path + ' --> [MP4] ' + artist[0] + ' | ' + album[0] + ' | ' + track[0]

  elif song_ext == 'mp3':
    audio = EasyID3(song_path)
    album = audio['album']
    artist = audio['artist']
    track = audio['title']

    print album_path + ' --> [MP3] ' + artist[0] + ' | ' + album[0] + ' | ' + track[0]
