from flask import render_template, redirect, request, Blueprint, session, url_for
import sys, os

from sqlalchemy import desc

reload(sys)
sys.setdefaultencoding('utf8')

artist = Blueprint('artist', __name__, template_folder='templates/artist')

from . import db, radio_player, CONFIG
from .models import Artist, Artist_Link
from .forms import ArtistForm, ImageForm, LinkForm

from sqlalchemy import desc

from radio import RadioPlayer

#################################################################################################################################
##  Artist
#################################################################################################################################

# ---> List Artists
@artist.route('/artist/list', methods=['GET'])
def artist_list():

    artist_list = Artist.query.all()

    session['last_url'] = url_for('artist.artist_list')

    template_page = 'artist_list.html'

    return render_template(template_page, artist_list=artist_list, radio_player=radio_player)

# ---> All Artists
@artist.route('/artist/all', methods=['GET'])
def artist_all():

    artist_list = Artist.query.order_by(desc(Artist.stars)).all()

    session['last_url'] = url_for('artist.artist_all')

    template_page = 'artist_grid.html'

    return render_template(template_page, artist_list=artist_list, radio_player=radio_player, title="All Artists")

# ---> Fav Artists
@artist.route('/artist/favorite', methods=['GET'])
def artist_favorite():

    artist_list = Artist.query.filter(Artist.fav==True).order_by(desc(Artist.stars)).all()

    session['last_url'] = url_for('artist.artist_favorite')

    template_page = 'artist_grid.html'

    return render_template(template_page, artist_list=artist_list, radio_player=radio_player, title="Favorite Artists")

# ---> Artist Styles
@artist.route('/artist/styles', methods=['GET'])
def artist_styles():

    artist_list = db.session.query(Artist.style).distinct()
    artist_styles = [ artist.style for artist in artist_list if artist.style != '' ]
    artist_styles.sort()


    session['last_url'] = url_for('artist.artist_styles')

    template_page = 'artist_styles.html'

    return render_template(template_page, artist_styles=artist_styles, radio_player=radio_player)

# ---> Artist Style
@artist.route('/artist/style/<style>', methods=['GET'])
def artist_style(style):

    artist_list = Artist.query.filter(Artist.style==style).order_by(desc(Artist.stars))

    session['last_url'] = url_for('artist.artist_style', style=style)

    template_page = 'artist_grid.html'

    return render_template(template_page, artist_list=artist_list, radio_player=radio_player, title=style)

# ---> Artist Countries
@artist.route('/artist/countries', methods=['GET'])
def artist_countries():

    artist_list = db.session.query(Artist.country).distinct()
    artist_countries = [ artist.country for artist in artist_list if artist.country != '' ]
    artist_countries.sort()

    session['last_url'] = url_for('artist.artist_countries')

    template_page = 'artist_countries.html'

    return render_template(template_page, artist_countries=artist_countries, radio_player=radio_player)

# ---> Artist County
@artist.route('/artist/country/<country>', methods=['GET'])
def artist_country(country):

    artist_list = Artist.query.filter(Artist.country==country).order_by(desc(Artist.stars))

    session['last_url'] = url_for('artist.artist_country', country=country)

    template_page = 'artist_grid.html'

    return render_template(template_page, artist_list=artist_list, radio_player=radio_player, title=country)

#################################################################################################################################
# Artist -> Show
#################################################################################################################################

# ---> Artist Show
@artist.route('/artist/show/<id>', methods=['GET'])
def artist_show(id):

    artist = Artist.query.filter_by(id=id).first()
    album_info = radio_player.artist_albums(artist)

    session['last_url'] = url_for('artist.artist_show', id=id)

    template_page = 'artist_show.html'

    return render_template(template_page, album_info=album_info, artist=artist, radio_player=radio_player, social_sites=CONFIG.SOCIAL_SITES)

# ---> Artist Album
@artist.route('/artist/album/<artist_id>/<album>', methods=['GET'])
def artist_album(artist_id,album):

    artist = Artist.query.filter_by(id=artist_id).first()
    songs_list = radio_player.album_songs(artist,album)
    album_info = radio_player.album_info(artist, album)

    session['last_url'] = url_for('artist.artist_album', artist_id=artist_id, album=album)

    template_page = 'artist_album_show.html'

    return render_template(template_page, artist=artist, album_info=album_info, songs_list=songs_list, radio_player=radio_player, social_sites=CONFIG.SOCIAL_SITES)

# ---> Load Album
@artist.route('/artist/album/load/<artist_id>/<album>', methods=['GET'])
def artist_album_load(artist_id,album):

    artist = Artist.query.filter_by(id=artist_id).first()
    songs_list = radio_player.album_songs(artist,album)
    radio_player.load_album(artist,album)

    redirect_page = url_for('artist.artist_album', artist_id=radio_player.artist.id, album=radio_player.album)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Song Play
@artist.route('/artist/album/song_play/<pos>', methods=['GET'])
def artist_album_song_play(pos):

    album = radio_player.album
    artist = radio_player.artist

    radio_player.play_song(pos)
    songs_list = radio_player.album_songs(artist,album)

    redirect_page = url_for('artist.artist_album', artist_id=radio_player.artist.id, album=radio_player.album)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


#################################################################################################################################
# Artist -> Add, Edit & Delete
#################################################################################################################################

# ---> Artist Add
@artist.route('/artist/add', methods=['GET', 'POST'])
def artist_add():

    form = ArtistForm()

    if form.validate_on_submit():

        name = form.name.data
        image_file = form.image_file.data
        country = form.country.data
        style = form.style.data

        image = name + '.png'

        description = ''
        stars = 1

        image_file.save(os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_ARTIST_IMG_DIR, image))

        artist = Artist(name=name,
                        image=image,
                        country=country,
                        description=description,
                        style=style,
                        stars=stars)

        db.session.add(artist)
        db.session.commit()

        artist_albums_path = os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_ALBUM_IMG_DIR, name)

        if not(os.path.exists(artist_albums_path)):
            os.mkdir(artist_albums_path)

        redirect_page = url_for('artist.artist_show', id=artist.id)
        session['last_url'] = redirect_page

        return redirect(redirect_page)


    session['last_url'] = url_for('artist.artist_add')

    template_page = 'artist_add.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Artist Edit
@artist.route('/artist/edit/<id>', methods=['GET', 'POST'])
def artist_edit(id):
    
    artist = Artist.query.filter_by(id=id).first()

    form = ArtistForm()

    if form.validate_on_submit():

        artist.name = form.name.data
        artist.description = form.description.data
        artist.image = form.image.data
        artist.country = form.country.data
        artist.style = form.style.data

        db.session.commit()

        redirect_page = url_for('artist.artist_show', id=artist.id)
        
        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = artist.name
    form.description.data = artist.description
    form.image.data = artist.image
    form.country.data = artist.country
    form.style.data = artist.style

    session['last_url'] = url_for('artist.artist_edit',id=id)

    template_page = 'artist_edit.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Artist Delete
@artist.route('/artist/delete/<id>', methods=['GET', 'POST'])
def artist_delete(id):

    artist = Artist.query.filter_by(id=id).first()

    for link in artist.artist_link_list :
        db.session.delete(link)

    db.session.delete(artist)
    db.session.commit()

    redirect_page = url_for('artist.artist_all', id=artist.id)
    
    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Artist Album Edit Image
@artist.route('/artist/album/edit_image/<id>/<album>', methods=['GET', 'POST'])
def artist_album_edit_image(id,album):

    artist = Artist.query.filter_by(id=id).first()

    form = ImageForm()

    if form.validate_on_submit():

        image_file = form.image_file.data

        image = album + '.png'

        image_file.save(os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_ALBUM_IMG_DIR, artist.name, image))
    
        redirect_page = url_for('artist.artist_album', artist_id=id, album=album)

        session['last_url'] = redirect_page

        return redirect(redirect_page)


    session['last_url'] = url_for('artist.artist_album_edit_image', id=id, album=album)

    template_page = 'artist_album_edit_image.html'

    return render_template(template_page, form=form,radio_player=radio_player)


#################################################################################################################################
# Artist Link -> Add, Edit & Delete
#################################################################################################################################

# ---> Artist Link Add
@artist.route('/artist/add_link/<id>', methods=['GET', 'POST'])
def artist_add_link(id):

    form = LinkForm()

    if form.validate_on_submit():

        name = form.name.data
        social_name = form.social_name.data
        url = form.url.data

        if social_name != 'none':
            name = social_name

        artist = Artist.query.filter_by(id=id).first()

        artist_link = Artist_Link(name=name,url=url,artist=artist)

        db.session.add(artist_link)
        db.session.commit()

        redirect_page = url_for('artist.artist_show',id=artist.id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)
    
    
    session['last_url'] = url_for('artist.artist_add_link',id=id)

    template_page = 'artist_add_link.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Artist Link Edit
@artist.route('/artist/edit_link/<id>', methods=['GET', 'POST'])
def artist_edit_link(id):

    artist_link = Artist_Link.query.filter_by(id=id).first()

    form = LinkForm()

    if form.validate_on_submit():

        artist_link.name = form.name.data
        artist_link.url = form.url.data

        db.session.commit()

        redirect_page = url_for('artist.artist_show',id=artist_link.artist_id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = artist_link.name
    form.url.data = artist_link.url

    session['last_url'] = url_for('artist.artist_edit_link',id=id)

    template_page = 'artist_edit_link.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Artist Link Delete
@artist.route('/artist/delete_link/<id>', methods=['GET'])
def artist_link_delete(id):
    artist_link = Artist_Link.query.filter_by(id=id).first()
    artist_id = artist_link.artist_id

    db.session.delete(artist_link)
    db.session.commit()

    redirect_page = url_for('artist.artist_show', id=artist_id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

###########################################################################################
## Fav, Unfav, Stars
###########################################################################################

# ---> Artist Fav
@artist.route('/artist_fav/<id>', methods=['GET'])
def artist_fav(id):
    artist = Artist.query.filter_by(id=id).first()

    artist.fav = True

    db.session.commit()

    redirect_page = url_for('artist.artist_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Artist UnFav
@artist.route('/artist_unfav/<id>', methods=['GET'])
def artist_unfav(id):
    artist = Artist.query.filter_by(id=id).first()

    artist.fav = False

    db.session.commit()

    redirect_page = url_for('artist.artist_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Artist Set Stars
@artist.route('/artist/stars/<id>/<stars>', methods=['GET'])
def artist_stars(id,stars):
    artist = Artist.query.filter_by(id=id).first()

    artist.stars = int(stars)

    db.session.commit()

    redirect_page = url_for('artist.artist_show',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)





