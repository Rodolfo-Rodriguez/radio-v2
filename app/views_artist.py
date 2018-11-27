from flask import render_template, redirect, request, Blueprint, session, url_for
import sys, os

reload(sys)
sys.setdefaultencoding('utf8')

artist = Blueprint('artist', __name__)

from . import db, radio_player, global_values
from .models import Artist

from sqlalchemy import desc

from radio import RadioPlayer

#################################################################################################################################
##  Artist
#################################################################################################################################

# ---> List Artists
@artist.route('/<client>/artist/list', methods=['GET'])
def artist_list(client):

    artist_list = Artist.query.all()

    session['last_url'] = url_for('artist.artist_list',client=client)

    template_page = client + '/artist_list.html'

    return render_template(template_page,artist_list=artist_list,radio_player=radio_player)

# ---> All Artists
@artist.route('/<client>/artist/all', methods=['GET'])
def artist_all(client):

    artist_list = Artist.query.all()

    session['last_url'] = url_for('artist.artist_all',client=client)

    template_page = client + '/artist_all.html'

    return render_template(template_page,artist_list=artist_list,radio_player=radio_player,title="All Artists")

# ---> Artist Albums
@artist.route('/<client>/artist/albums/<id>', methods=['GET'])
def artist_albums(client,id):

    artist = Artist.query.filter_by(id=id).first()
    album_list = radio_player.artist_albums(artist)

    session['last_url'] = url_for('artist.artist_albums',client=client,id=id)

    template_page = client + '/artist_albums.html'

    return render_template(template_page,album_list=album_list,artist=artist,radio_player=radio_player)

# ---> Artist Album
@artist.route('/<client>/artist/album/<artist_id>/<album>', methods=['GET'])
def artist_album(client,artist_id,album):

    artist = Artist.query.filter_by(id=artist_id).first()
    songs_list = radio_player.album_songs(artist,album)

    session['last_url'] = url_for('artist.artist_album',client=client,artist_id=artist_id,album=album)

    template_page = client + '/album_songs.html'

    return render_template(template_page,artist=artist,album=album,songs_list=songs_list,radio_player=radio_player)

# ---> Load Album
@artist.route('/<client>/album/play/<artist_id>/<album>', methods=['GET'])
def album_play(client,artist_id,album):

    artist = Artist.query.filter_by(id=artist_id).first()
    songs_list = radio_player.album_songs(artist,album)
    radio_player.load_album(artist,album)

    session['last_url'] = url_for('artist.artist_album',client=client,artist_id=artist_id,album=album)

    template_page = client + '/album_songs.html'

    return render_template(template_page,artist=artist,album=album,songs_list=songs_list,radio_player=radio_player)

# ---> Song Play
@artist.route('/<client>/song/play/<pos>', methods=['GET'])
def song_play(client,pos):

    album = radio_player.album
    artist = radio_player.artist

    radio_player.play_song(pos)
    songs_list = radio_player.album_songs(artist,album)

    session['last_url'] = url_for('artist.artist_album',client=client,artist_id=artist.id,album=album)

    template_page = client + '/album_songs.html'

    return render_template(template_page,artist=artist,album=album,songs_list=songs_list,radio_player=radio_player)


# ---> Artist Styles
@artist.route('/<client>/artist/styles', methods=['GET'])
def artist_styles(client):

    artist_list = db.session.query(Artist.style).distinct()
    artist_styles = []
    for artist in artist_list:
        if (artist.style != ''):
            artist_styles.append(artist.style)

    session['last_url'] = url_for('artist.artist_styles',client=client)

    template_page = client + '/artist_styles.html'

    return render_template(template_page,artist_styles=artist_styles,radio_player=radio_player)

# ---> Artist Style
@artist.route('/<client>/artist/style/<style>', methods=['GET'])
def artist_style(client,style):

    artist_list = Artist.query.filter(Artist.style==style)

    session['last_url'] = url_for('artist.artist_style',client=client,style=style)

    template_page = client + '/artist_all.html'

    return render_template(template_page,artist_list=artist_list,radio_player=radio_player,title=style)

# ---> Artist Countries
@artist.route('/<client>/artist/countries', methods=['GET'])
def artist_countries(client):

    artist_list = db.session.query(Artist.country).distinct()
    artist_countries = []
    for artist in artist_list:
        if (artist.country != ''):
            artist_countries.append(artist.country)

    session['last_url'] = url_for('artist.artist_countries',client=client)

    template_page = client + '/artist_countries.html'

    return render_template(template_page,artist_countries=artist_countries,radio_player=radio_player)

# ---> Artist County
@artist.route('/<client>/artist/country/<country>', methods=['GET'])
def artist_country(client,country):

    artist_list = Artist.query.filter(Artist.country==country)

    session['last_url'] = url_for('artist.artist_country',client=client,country=country)

    template_page = client + '/artist_all.html'

    return render_template(template_page,artist_list=artist_list,radio_player=radio_player,title=country)

#################################################################################################################################
# Artist -> Add, Edit & Delete
#################################################################################################################################

# ---> Artist Add
@artist.route('/artist/add', methods=['GET', 'POST'])
def artist_add():

    session['last_url'] = url_for('artist.artist_add')

    return render_template('web/artist_add.html',radio_player=radio_player)

# ---> Artist Add Commit
@artist.route('/artist/add_commit', methods=['GET', 'POST'])
def artist_add_commit():

    name = request.form.get("name")
    country = request.form.get("country")
    description = request.form.get("description")
    style = request.form.get("style")
    image_file = request.files["image_file"]

    image = name + '.png'

    image_file.save(os.path.join(global_values.artist_images_dir, image))

    artist = Artist(name=name,image=image,country=country,description=description,style=style)

    db.session.add(artist)
    db.session.commit()

    artist_albums_path = os.path.join(global_values.albums_images_dir, name)

    if not(os.path.exists(artist_albums_path)):
        os.mkdir(artist_albums_path)

    artist = Artist.query.filter_by(name=name).first()

    redirect_page = url_for('artist.artist_albums',client='web',id=artist.id)
    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Artist Edit
@artist.route('/artist/edit/<id>', methods=['GET'])
def artist_edit(id):
    artist = Artist.query.filter_by(id=id).first()

    session['last_url'] = url_for('artist.artist_edit',id=id)

    return render_template('web/artist_edit.html',artist=artist,radio_player=radio_player)

# ---> Artist Edit Commit
@artist.route('/artist/edit_commit/<id>', methods=['GET', 'POST'])
def artist_edit_commit(id):
    artist = Artist.query.filter_by(id=id).first()

    artist.name = request.form.get("name")
    artist.image = request.form.get("image")
    artist.country = request.form.get("country")
    artist.description = request.form.get("description")
    artist.style = request.form.get("style")
    artist.stars = request.form.get("stars")

    db.session.commit()

    redirect_page = url_for('artist.artist_albums',client='web',id=artist.id)
    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Artist Album Edit
@artist.route('/album/edit/<id>/<album>', methods=['GET'])
def album_edit(id,album):
    artist = Artist.query.filter_by(id=id).first()

    session['last_url'] = url_for('artist.album_edit',id=id,album=album)

    return render_template('web/album_edit.html',artist=artist,album=album,radio_player=radio_player)


# ---> Album Add Commit
@artist.route('/album/edit_commit/<id>/<album>', methods=['GET', 'POST'])
def album_edit_commit(id,album):

    artist = Artist.query.filter_by(id=id).first()

    album_image = album + '.png'

    image_file = request.files["image_file"]

    image_file.save(os.path.join(global_values.albums_images_dir, artist.name, album_image))

    redirect_page = url_for('artist.artist_album', client='web', artist_id=id, album=album)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


