#!/usr/bin/python2

import sys

from mutagen import File


if len(sys.argv) < 2:
  print '[ERROR] Uso: ' + sys.argv[0] + ' [filename]'
  sys.exit(2)

filename = sys.argv[1]

audio = File(filename)

print audio.pprint()

artist = audio['TPE1']
print str(artist)

#artist = audio['TPE1']
#artwork = audio['APIC:'].data

#with open('image.png', 'wb') as img:
   #img.write(artwork) # write artwork to new image
