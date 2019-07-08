#!/usr/bin/python2

import sys

sys.path.append('/home/pi/develop/radio-v3/app')

from feed_manager import FeedManager

# if len(sys.argv) < 2:
#   print '[ERROR] Uso: {} [url]'.format(sys.argv[0])
#   sys.exit(2)

# url = sys.argv[1]

#url = 'https://espectador.com/otroelefante/maxiguerra/las-vidas-extras-de-wilko-johnson'
#url = 'https://delsol.uy/lamesa/deporgol/ranchero-con-detalles-de-la-gira-de-penarol-en-estados-unidos'
#url = 'https://delsol.uy/notoquennada/ntnconcentrado/miranda-y-la-union-ultraderechista-talvi-y-la-renovacion-cosse-y-su-aporte-en-la-campana'
url = 'https://delsol.uy/copaamerica/audios/sol_13671'

feed_manager = FeedManager(url)
#title = feed_manager.get_title()
audio_url = feed_manager.get_audio_url()
#pub_date = feed_manager.get_pub_date()

#print title
print audio_url
#print pub_date 
