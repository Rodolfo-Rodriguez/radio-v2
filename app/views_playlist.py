from flask import render_template, redirect, request, Blueprint, session, url_for, flash
import sys

reload(sys)
sys.setdefaultencoding('utf8')

playlist = Blueprint('playlist', __name__, template_folder='templates/playlist')

from .models import Radios, Artist, Playlist, Podcast
from .forms import PlaylistForm
from . import db, radio_player

from sqlalchemy import desc

from radio import RadioPlayer

###########################################################################################
# List, Show
###########################################################################################

# ---> Playlist List
@playlist.route('/playlist/list', methods=['GET'])
def playlist_list():

    playlist_list = Playlist.query.all()

    session['last_url'] = url_for('playlist.playlist_list')

    return render_template('playlist_list.html',playlist_list=playlist_list,radio_player=radio_player)

# ---> All Playlist
@playlist.route('/playlist/all', methods=['GET'])
def playlist_all():

    playlist_list = Playlist.query.all()

    session['last_url'] = url_for('playlist.playlist_all')

    template_page = 'playlist_grid.html'
    
    return render_template(template_page,playlist_list=playlist_list,radio_player=radio_player,title='All Playlist')


# ---> Playlist Types
@playlist.route('/playlist/type', methods=['GET'])
def playlist_types():

    playlist_list = db.session.query(Playlist.type).distinct()
    playlist_types = [ playlist.type for playlist in playlist_list if playlist.type != '' ]
    playlist_types.sort()
    
    session['last_url'] = url_for('playlist.playlist_types')

    template_page = 'playlist_types.html'

    return render_template(template_page,playlist_types=playlist_types,radio_player=radio_player)


# ---> Playlist Type
@playlist.route('/playlist/type/<type>', methods=['GET'])
def playlist_type(type):

    playlist_list = Playlist.query.filter(Playlist.type==type)

    session['last_url'] = url_for('playlist.playlist_type',type=type)

    template_page = 'playlist_grid.html'

    return render_template(template_page,playlist_list=playlist_list,radio_player=radio_player,title=type)


# ---> Playlist Show
@playlist.route('/playlist/show/<id>', methods=['GET'])
def playlist_show(id):

    playlist = Playlist.query.filter_by(id=id).first()

    songs_list = radio_player.playlist_songs(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_show',id=id)

    template_page = 'playlist_show.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


###########################################################################################
# Load, Play
###########################################################################################

# ---> Playlist Load
@playlist.route('/playlist/load/<id>', methods=['GET'])
def playlist_load(id):

    playlist = Playlist.query.filter_by(id=id).first()

    songs_list = radio_player.playlist_songs(playlist.playlist)

    radio_player.load_playlist(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_show',id=id)

    template_page = 'playlist_show.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)


# ---> Playlist Play Song
@playlist.route('/playlist/play_song/<id>/<pos>', methods=['GET'])
def playlist_play_song(id,pos):

    playlist = Playlist.query.filter_by(id=id).first()

    radio_player.play_song(pos)

    songs_list = radio_player.playlist_songs(playlist.playlist)

    session['last_url'] = url_for('playlist.playlist_show',id=id)

    template_page = 'playlist_show.html'

    return render_template(template_page,playlist=playlist,songs_list=songs_list,radio_player=radio_player)

###########################################################################################
# Add, Edit, Delete
###########################################################################################

# ---> Playlist Add
@playlist.route('/playlist/add', methods=['GET', 'POST'])
def playlist_add():

    form = PlaylistForm()

    if form.validate_on_submit():

        name = form.name.data
        image = form.image.data
        playlist_name = form.playlist.data
        description = ''
        type = ''
        
        playlist = Playlist(name=name,
                            image=image,
                            playlist=playlist_name,
                            description=description,
                            type=type)

        db.session.add(playlist)
        db.session.commit()

        redirect_page = url_for('playlist.playlist_show', id=playlist.id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)
    
    
    session['last_url'] = url_for('playlist.playlist_add')

    return render_template('playlist_add.html',radio_player=radio_player,form=form)

# ---> Playlist Edit
@playlist.route('/playlist/edit/<id>', methods=['GET', 'POST'])
def playlist_edit(id):

    playlist = Playlist.query.filter_by(id=id).first()

    form = PlaylistForm()

    if form.validate_on_submit():

        playlist.name = form.name.data
        playlist.image = form.image.data
        playlist.playlist = form.playlist.data
        playlist.description = form.description.data
        playlist.type = form.type.data

        db.session.commit()

        redirect_page = url_for('playlist.playlist_show', id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = playlist.name
    form.image.data = playlist.image
    form.playlist.data = playlist.playlist
    form.description.data = playlist.description
    form.type.data = playlist.type
    
    session['last_url'] = url_for('playlist.playlist_edit', id=id)

    return render_template('playlist_edit.html',form=form,radio_player=radio_player)


# ---> Playlist Delete
@playlist.route('/playlist/delete/<id>', methods=['GET'])
def playlist_delete(id):

    playlist = Playlist.query.filter_by(id=id).first()
    
    db.session.delete(playlist)
    db.session.commit()

    redirect_page = url_for('playlist.playlist_all')

    session['last_url'] = redirect_page

    return redirect(redirect_page)
