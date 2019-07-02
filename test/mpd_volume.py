#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-1'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)

status = client.status()
volume = status['volume']

client.setvol(72)

print volume

client.close()
client.disconnect()
