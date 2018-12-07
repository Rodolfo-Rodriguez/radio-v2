#!/usr/bin/python2

from mpd import MPDClient

mpd_client = 'rune-1'
mpd_port = '6600'

client = MPDClient()

client.connect(mpd_client, mpd_port)

playlists = client.listplaylists()
current = client.currentsong()
status = client.status()
playlist = client.playlist()
playlist_info = client.playlistinfo()

saved_playlist = client.listplaylistinfo('ElectronicGroove')

artist = 'Led Zeppelin'
album = 'Coda'
#alb_list = client.list('title','album',album,'artist',artist)
alb_list = client.list('album','artist',artist)
date_list = client.list('date','artist',artist)

album_info = []
for album in alb_list:
    alb_date = client.list('date','artist',artist,'album',album)[0]
    album_info.append({'date':alb_date,'album':album})

album_info.sort(key=lambda x: x['date'])

#print album_info

search_res = client.find('album','The Queen Is Dead','artist','The Smiths')

print "########## Status ##########"
print status
print '\n'

print "########## Current ##########"
print current
print '\n'

# print "########## Playlists ##########"
# print playlists
# print '\n'

# print "########## PlayList ##########"
# print playlist
# print '\n'

# print "########## PlayList Info ##########"
# print playlist_info
# print '\n'

# print "########## List  ##########"
# print alb_list
# print date_list
# print '\n'

# print "########## Search  ##########"
# print search_res
# print '\n'

# print "########## Saved Playlist  ##########"
# print saved_playlist
# print '\n'
