
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys

reload(sys)
sys.setdefaultencoding('utf8')

player = Blueprint('player', __name__, template_folder='templates/base')

from .models import Radios, Artist, Playlist, Podcast
from . import db, radio_player
from .forms import URLForm

from sqlalchemy import desc

from radio import RadioPlayer
from podcast import PodcastInfo


###########################################################################################
##  Controls
###########################################################################################

# ---> Play

@player.route('/play', methods=['GET'])
def play():
    radio_player.play()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Stop

@player.route('/stop', methods=['GET'])
def stop():
    radio_player.stop()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Pause
@player.route('/pause', methods=['GET'])
def pause():
    radio_player.pause()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Next
@player.route('/next', methods=['GET'])
def next():
    radio_player.next()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Previous
@player.route('/previous', methods=['GET'])
def previous():
    radio_player.previous()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> SeekPlus

@player.route('/seekplus/<time_interval>', methods=['GET'])
def seekplus(time_interval):
    radio_player.seekplus(time_interval)

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> SeekLess

@player.route('/seekless/<time_interval>', methods=['GET'])
def seekless(time_interval):
    radio_player.seekless(time_interval)

    redirect_page = session['last_url']

    return redirect(redirect_page)

 #---> Play Song Pos

@player.route('/play_song/<pos>', methods=['GET'])
def play_song_pos(pos):
    
    radio_player.play_song(pos)

    redirect_page = session['last_url']

    return redirect(redirect_page)

 #---> Play Song Pos

@player.route('/play_url', methods=['GET', 'POST'])
def play_url():

    form = URLForm()

    if form.validate_on_submit():

        url = form.url.data
    
        radio_player.play_url(url)

        redirect_page = '/'

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    session['last_url'] = url_for('player.play_url')

    template_page = 'play_url.html'

    return render_template(template_page, form=form, radio_player=radio_player)


###########################################################################################
##  Server
###########################################################################################

# ---> Disconnect from Server

@player.route('/mpd_disconnect', methods=['GET'])
def server_disconnect():
    radio_player.disconnect()
    return redirect('/')

# ---> Server

@player.route('/mpd_client/<hostname>', methods=['GET'])
def server(hostname):
    radio_player.connect(hostname)
    return redirect('/')

