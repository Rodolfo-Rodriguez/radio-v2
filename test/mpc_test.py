#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-1v2'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)

#playlist_name = 'AppsMac'

#plinfo = client.listplaylistinfo(playlist_name)

#print plinfo

outputs = client.outputs()

print outputs


client.close()
client.disconnect()


