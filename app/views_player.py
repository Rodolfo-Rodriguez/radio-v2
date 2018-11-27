
from flask import render_template, redirect, request, Blueprint, session
import sys

reload(sys)
sys.setdefaultencoding('utf8')

player = Blueprint('player', __name__)

from .models import Radios, Artist, Playlist, Podcast
from . import db, radio_player

from sqlalchemy import desc

from radio import RadioPlayer
from podcast import PodcastInfo


# ---> Play

@player.route('/<client>/play', methods=['GET'])
def play(client):
    radio_player.play()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Stop

@player.route('/<client>/stop', methods=['GET'])
def stop(client):
    radio_player.stop()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Pause
@player.route('/<client>/pause', methods=['GET'])
def pause(client):
    radio_player.pause()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Next
@player.route('/<client>/next', methods=['GET'])
def next(client):
    radio_player.next()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Previous
@player.route('/<client>/previous', methods=['GET'])
def previous(client):
    radio_player.previous()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> SeekPlus

@player.route('/<client>/seekplus/<time_interval>', methods=['GET'])
def seekplus(client,time_interval):
    radio_player.seekplus(time_interval)

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> SeekLess

@player.route('/<client>/seekless/<time_interval>', methods=['GET'])
def seekless(client,time_interval):
    radio_player.seekless(time_interval)

    redirect_page = '/'

    return redirect(redirect_page)

###########################################################################################
##  Server
###########################################################################################

# ---> Server

@player.route('/mpd_client/<hostname>', methods=['GET'])
def server(hostname):
    radio_player.mpd_client = hostname
    return redirect('/')
