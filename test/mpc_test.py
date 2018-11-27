#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-2'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)

artist = 'La Vela Puerca'

alb_list = client.list('album','artist',artist)

print "########## Search  ##########"
print alb_list
print '\n'


client.close()
client.disconnect()
