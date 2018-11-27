from flask import render_template, redirect, request, Blueprint, session, url_for
import sys

reload(sys)
sys.setdefaultencoding('utf8')

playlist = Blueprint('playlist', __name__)

from .models import Radios, Artist, Playlist, Podcast
from . import db, radio_player

from sqlalchemy import desc

from radio import RadioPlayer

###########################################################################################
# Playlists
###########################################################################################

# ---> Mobile Playlists Menu
@playlist.route('/mobile/playlists', methods=['GET'])
def mobile_playlists():
    return render_template('mobile/playlists_menu.html')


# ---> All Playlist
@playlist.route('/<client>/playlist/all', methods=['GET'])
def playlist_all(client):

    playlist_list = Playlist.query.all()

    session['last_url'] = url_for('playlist.playlist_all',client=client)

    template_page = client + '/playlist_all.html'
    
    return render_template(template_page,playlist_list=playlist_list,radio_player=radio_player,title='All Playlist')


# ---> Playlist Types
@playlist.route('/<client>/playlist/type', methods=['GET'])
def playlist_types(client):

    playlist_list = db.session.query(Playlist.type).distinct()
    playlist_types = []
    for playlist in playlist_list:
        if (playlist.type != ''):
            playlist_types.append(playlist.type)

    session['last_url'] = url_for('playlist.playlist_types',client=client)

    template_page = client + '/playlist_types.html'

    return render_template(template_page,playlist_types=playlist_types,radio_player=radio_player)


# ---> Playlist Type
@playlist.route('/<client>/playlist/type/<type>', methods=['GET'])
def playlist_type(client,type):

    playlist_list = Playlist.query.filter(Playlist.type==type)

    session['last_url'] = url_for('playlist.playlist_type',client=client,type=type)

    template_page = client + '/playlist_all.html'

    return render_template(template_page,playlist_list=playlist_list,radio_player=radio_player,title=type)


# ---> Playlist Songs
@playlist.route('/<client>/playlist/songs/<id>', methods=['GET'])
def playlist_songs(client,id):

    playlist = Playlist.query.filter_by(id=id).first()

    songs_list = radio_player.playlist_songs(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_songs',client=client,id=id)

    template_page = client + '/playlist_songs.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


# ---> Playlist Songs PL
@playlist.route('/<client>/playlist/songs_pl/<pl>', methods=['GET'])
def playlist_songs_pl(client,pl):

    playlist = Playlist.query.filter_by(playlist=pl).first()

    songs_list = radio_player.playlist_songs(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_songs_pl',client=client,pl=pl)

    template_page = client + '/playlist_songs.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


# ---> Playlist Load
@playlist.route('/<client>/playlist/load/<id>', methods=['GET'])
def playlist_load(client,id):

    playlist = Playlist.query.filter_by(id=id).first()

    songs_list = radio_player.playlist_songs(playlist.playlist)

    radio_player.load_playlist(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_songs',client=client,id=id)

    template_page = client + '/playlist_songs.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


# ---> Playlist Play Song
@playlist.route('/<client>/playlist/play_song/<id>/<pos>', methods=['GET'])
def playlist_play_song(client,id,pos):

    playlist = Playlist.query.filter_by(id=id).first()

    radio_player.play_song(pos)

    songs_list = radio_player.playlist_songs(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_play_song',client=client,id=id,pos=pos)

    template_page = client + '/playlist_songs.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


# ---> Playlist Stop
@playlist.route('/<client>/playlist/stop', methods=['GET'])
def playlist_playlist_stop(client):

    playlist = radio_player.playlist

    songs_list = radio_player.playlist_songs(playlist)

    radio_player.stop()

    session['last_url'] = url_for('playlist.playlist_play_song',client=client,id=id,pos=pos)

    template_page = client + '/playlist_songs.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


# ---> Playlist Add
@playlist.route('/playlist/add', methods=['GET', 'POST'])
def playlist_add():

    session['last_url'] = url_for('playlist.playlist_add')

    return render_template('web/playlist_add.html',radio_player=radio_player)

# ---> Playlist Add Commit
@playlist.route('/playlist/add_commit', methods=['GET', 'POST'])
def playlist_add_commit():

    name = request.form.get("name")
    image = request.form.get("image")
    playlist_name = request.form.get("playlist")

    playlist = Playlist(name=name,image=image,playlist=playlist_name)

    db.session.add(playlist)
    db.session.commit()

    pl = Playlist.query.filter_by(name=name).first()

    redirect_page = url_for('playlist.playlist_songs', client='web', id=pl.id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Playlist Edit
@playlist.route('/playlist/edit/<id>', methods=['GET'])
def playlist_edit(id):
    playlist = Playlist.query.filter_by(id=id).first()

    session['last_url'] = url_for('playlist.playlist_edit', id=id)

    return render_template('web/playlist_edit.html',playlist=playlist,radio_player=radio_player)

# ---> Playlist Edit Commit
@playlist.route('/playlist/edit_commit/<id>', methods=['GET', 'POST'])
def playlist_edit_commit(id):
    playlist = Playlist.query.filter_by(id=id).first()

    playlist.name = request.form.get("name")
    playlist.image = request.form.get("image")
    playlist.playlist = request.form.get("playlist")
    playlist.description = request.form.get("description")
    playlist.type = request.form.get("type")

    db.session.commit()

    redirect_page = url_for('playlist.playlist_songs', client='web', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Playlist Delete
@playlist.route('/playlist/delete/<id>', methods=['GET'])
def playlist_delete(id):
    playlist = Playlist.query.filter_by(id=id).first()
    db.session.delete(playlist)
    db.session.commit()

    redirect_page = url_for('playlist.playlist_all', client='web')

    session['last_url'] = redirect_page

    return redirect(redirect_page)
