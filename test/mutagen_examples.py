#!/usr/bin/python2

import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mutagen import File

line_sep_1 = '#' * 100
line_sep_2 = '-' * 100

# Create MP4 Metadata Object

audio = MP4("Gin.m4a")

# Read Tags

track = audio['\xa9nam']
artist = audio['\xa9ART']
album = audio['\xa9alb']

print line_sep_1
print 'Tags'
print line_sep_2

print 'Track: ' + track[0]
print 'Artist:' + artist[0]
print 'Album:' + album[0]

# Metadata string

text_tag = audio.pprint()

print line_sep_1
print 'Metadata Text'
print line_sep_2

print text_tag

# File Cover

cover = audio['covr']
image = cover[0]

# Write Cover to File

open('test.jpg','wb').write(cover[0])

# Audio Info

audio_info = audio.info
audio_info_text = audio_info.pprint()

print line_sep_1
print 'Audio Info'
print line_sep_2

print audio_info_text

# Write Tags

audio['\xa9nam'] = u"Track Name"
audio['\xa9ART'] = u"Artist"
audio['\xa9alb'] = u"Album"

audio.save()
