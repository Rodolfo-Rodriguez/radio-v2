#!/usr/bin/python2

import sys
import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File


if len(sys.argv) < 2:
  print '[ERROR] Uso: ' + sys.argv[0] + ' [filename]'
  sys.exit(2)

filename = sys.argv[1]

# Create MP4 Metadata Object

audio = MP4(filename)

# Read Tags

track = audio['\xa9nam']
artist = audio['\xa9ART']
album = audio['\xa9alb']

cover_filename = album[0] + '.png'

# File Cover

cover = audio['covr']
image = cover[0]

# Write Cover to File

open(cover_filename,'wb').write(cover[0])

