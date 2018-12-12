
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys, os

from sqlalchemy import desc

reload(sys)
sys.setdefaultencoding('utf8')

base = Blueprint('base', __name__, template_folder='templates/base')

from . import db, radio_player, CONFIG, db_manager

from radio import RadioPlayer

###########################################################################################
# Home
###########################################################################################

# ---> Home
@base.route('/', methods=['GET'])
def home():

    radio_player.disconnect()
    radio_player.update_fav_radios()

    session['last_url'] = '/'

    template_page = 'home.html'

    return render_template(template_page, radio_player=radio_player,db_manager=db_manager)

###########################################################################################
##  Playing
###########################################################################################

# ---> Current Playlist
@base.route('/playing', methods=['GET'])
def playling():

    if (radio_player.loaded=='album'):

        redirect_page = url_for('artist.artist_album', artist_id=radio_player.artist.id, album=radio_player.album)

    elif (radio_player.loaded=='radio'):

        redirect_page = url_for('radio.radio_show', id=radio_player.radio.id)

    elif (radio_player.loaded=='playlist'):

        redirect_page = url_for('playlist.playlist_show', id=radio_player.playlist.id)

    elif (radio_player.loaded=='podcast'):

        redirect_page = url_for('podcast.podcast_show', id=radio_player.podcast.id)

    else:
        redirect_page = url_for('base.home')

    session['last_url'] = redirect_page
    
    return redirect(redirect_page)

