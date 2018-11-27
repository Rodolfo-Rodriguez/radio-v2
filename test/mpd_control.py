#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-1'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)

status = client.status()
elapsed = float(status['elapsed'])

song = client.currentsong()

print status
print song

#client.seekcur(elapsed + 60)

client.close()
client.disconnect()
