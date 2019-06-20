#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-1v2'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)


uri = "USB/WD-500/Podcasts"

client.update(uri)


client.close()
client.disconnect()


