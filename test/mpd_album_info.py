#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-1'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)

search_res = client.find('album','The Queen Is Dead','artist','The Smiths')[0]

album_list = client.list('album','artist','The Smiths')

print "########## Search  ##########"
print search_res
print '\n'

print "########## Search  ##########"
print album_list
print '\n'
