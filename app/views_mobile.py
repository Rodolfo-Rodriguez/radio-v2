
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys, os, time

from sqlalchemy import desc

reload(sys)
sys.setdefaultencoding('utf8')

mobile = Blueprint('mobile', __name__, template_folder='templates/mobile')

from . import db, radio_player, CONFIG, db_manager
from .models import Radios, Program, Artist, Playlist, Podcast, Radio_Link, Bookmark, Preset
from .forms import BookmarkForm

from radio import RadioPlayer, Bookmark

###########################################################################################
# Mobile
###########################################################################################

# ---> Mobile Home
@mobile.route('/mobile', methods=['GET'])
def mobile_home():

    #radio_player.disconnect()

    session['last_url'] = url_for('mobile.mobile_home')

    return render_template('mobile_home.html', radio_player=radio_player)

###########################################################################################
# Mobile Radio Menus
###########################################################################################

# ---> Radios Menu
@mobile.route('/mobile/radio/menu', methods=['GET'])
def mobile_radio_menu():

    session['last_url'] = url_for('mobile.mobile_radio_menu')

    return render_template('mobile_radio_menu.html', radio_player=radio_player)


# ---> Radios List Style
@mobile.route('/mobile/radio/list/<filter_type>/<filter_value>', methods=['GET'])
def mobile_radio_list(filter_type, filter_value):

    if filter_type == 'all':
        radio_list = Radios.query.all()
    elif filter_type == 'favorite':
        radio_list = Radios.query.filter(Radios.fav==True).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()        
    elif filter_type == 'style':
        radio_list = Radios.query.filter(Radios.style==filter_value).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()
    elif filter_type == 'country':
        radio_list = Radios.query.filter(Radios.country==filter_value).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()
    elif filter_type == 'stars':
        radio_list = Radios.query.filter(Radios.stars==filter_value).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()

    radio_player.update_state(radio_list)

    session['last_url'] = url_for('mobile.mobile_radio_list', filter_type=filter_type, filter_value=filter_value)

    return render_template('mobile_radio_list.html',radio_player=radio_player, radio_list=radio_list)


# ---> Radio Filter List
@mobile.route('/mobile/radio/filter_list/<filter_type>', methods=['GET'])
def mobile_radio_filter_list(filter_type):

    if filter_type == 'style':
        radio_list = db.session.query(Radios.style).distinct()
        radio_items = [ radio.style for radio in radio_list if radio.style != '']
        radio_items.sort()
    elif filter_type == 'country':
        radio_list = db.session.query(Radios.country).distinct()
        radio_items = [ radio.country for radio in radio_list if radio.country != '' ]
        radio_items.sort()
    elif filter_type == 'stars':
        radio_list = db.session.query(Radios.stars).distinct()
        radio_items = [ radio.stars for radio in radio_list if radio.stars != '' ]
        radio_items.sort()

    session['last_url'] = url_for('mobile.mobile_radio_filter_list', filter_type=filter_type)

    return render_template('mobile_radio_filter_list.html', radio_player=radio_player, filter_type=filter_type ,radio_items=radio_items)



# ---> Radio Presets Grid
@mobile.route('/mobile/radio/presets', methods=['GET'])
def mobile_radio_presets():

    preset_list = Preset.query.all()

    session['last_url'] = url_for('mobile.mobile_radio_presets')

    return render_template('mobile_preset_list.html', radio_player=radio_player, preset_list=preset_list)


###########################################################################################
# Mobile Artist Menus
###########################################################################################

# ---> Artist Menu
@mobile.route('/mobile/artist/menu', methods=['GET'])
def mobile_artist_menu():

    session['last_url'] = url_for('mobile.mobile_artist_menu')

    return render_template('mobile_artist_menu.html', radio_player=radio_player)

# ---> Artist List Style
@mobile.route('/mobile/artist/list/<filter_type>/<filter_value>', methods=['GET'])
def mobile_artist_list(filter_type, filter_value):

    if filter_type == 'all':
        artist_list = Artist.query.all()
    elif filter_type == 'favorite':
        artist_list = Artist.query.filter(Artist.fav==True).all()     
    elif filter_type == 'style':
        artist_list = Artist.query.filter(Artist.style==filter_value).all()
    elif filter_type == 'country':
        artist_list = Artist.query.filter(Artist.country==filter_value).all()
    elif filter_type == 'stars':
        artist_list = Artist.query.filter(Artist.stars==filter_value).all()

    session['last_url'] = url_for('mobile.mobile_artist_list', filter_type=filter_type, filter_value=filter_value)

    return render_template('mobile_artist_list.html',radio_player=radio_player, artist_list=artist_list)


# ---> Artist Filter List
@mobile.route('/mobile/artist/filter_list/<filter_type>', methods=['GET'])
def mobile_artist_filter_list(filter_type):

    if filter_type == 'style':
        artist_list = db.session.query(Artist.style).distinct()
        artist_items = [ artist.style for artist in artist_list if artist.style != '']
        artist_items.sort()
    elif filter_type == 'country':
        artist_list = db.session.query(Artist.country).distinct()
        artist_items = [ artist.country for artist in artist_list if artist.country != '' ]
        artist_items.sort()
    elif filter_type == 'stars':
        artist_list = db.session.query(Artist.stars).distinct()
        artist_items = [ artist.stars for artist in artist_list if artist.stars != '' ]
        artist_items.sort()

    session['last_url'] = url_for('mobile.mobile_artist_filter_list', filter_type=filter_type)

    return render_template('mobile_artist_filter_list.html', radio_player=radio_player, filter_type=filter_type ,artist_items=artist_items)


# ---> Artist Menu
@mobile.route('/mobile/artist/show/<id>', methods=['GET'])
def mobile_artist_show(id):

    artist = Artist.query.filter_by(id=id).first()
    album_info = radio_player.artist_albums(artist)

    session['last_url'] = url_for('mobile.mobile_artist_show', id=id)

    return render_template('mobile_artist_show.html', radio_player=radio_player, album_info=album_info, artist=artist)


# ---> Load Album
@mobile.route('/mobile/artist/album/load/<artist_id>/<album>', methods=['GET'])
def mobile_artist_album_load(artist_id,album):

    artist = Artist.query.filter_by(id=artist_id).first()
    songs_list = radio_player.album_songs(artist,album)
    radio_player.load_album(artist,album)

    redirect_page = url_for('mobile.mobile_player')

    session['last_url'] = redirect_page

    return redirect(redirect_page)


###########################################################################################
# Mobile Play, Stop
###########################################################################################

# ---> Power
@mobile.route('/mobile/power', methods=['GET'])
def mobile_power():
    radio_player.power()

    redirect_page = session['last_url']

    return redirect(redirect_page)


# ---> Volume Up
@mobile.route('/mobile/vol_up', methods=['GET'])
def mobile_vol_up():
    radio_player.vol_up()

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Volume Down
@mobile.route('/mobile/vol_down', methods=['GET'])
def mobile_vol_down():
    radio_player.vol_down()

    redirect_page = session['last_url']

    return redirect(redirect_page)


# ---> Player
@mobile.route('/mobile/player', methods=['GET'])
def mobile_player():

    session['last_url'] = url_for('mobile.mobile_player')

    if radio_player.server_type == 'CXN':
        preset_id = radio_player.preset_playing
        preset = Preset.query.filter_by(id=preset_id).first()
        if preset:
            radio = preset.radios
        else:
            radio = None
            
        return render_template('mobile_cxn_player.html',radio_player=radio_player, radio=radio)
    else:
        return render_template('mobile_player.html',radio_player=radio_player)



# ---> Playlist
@mobile.route('/mobile/show/playlist', methods=['GET'])
def mobile_show_playlist():

    session['last_url'] = url_for('mobile.mobile_show_playlist')
    
    return render_template('mobile_show_playlist.html',radio_player=radio_player)


# ---> Radios Play
@mobile.route('/mobile/radio/play/<id>', methods=['GET'])
def mobile_radio_play(id):

    radio = Radios.query.filter_by(id=id).first()
    preset_id = radio.preset_number()

    session['last_url'] = url_for('mobile.mobile_player')

    if radio_player.server_type == 'CXN':
        if preset_id > 0:
            radio_player.cxn_play_preset(preset_id)
            time.sleep(4)
            radio_player.update_server_status()

            return render_template('mobile_cxn_player.html',radio_player=radio_player, radio=radio)
    else:
        radio_player.playradio(radio)
        return render_template('mobile_player.html',radio_player=radio_player)
    
    

# ---> Stop

@mobile.route('/mobile/stop', methods=['GET'])
def mobile_stop():
    radio_player.stop()

    return redirect(session['last_url'])

# ---> Play

@mobile.route('/mobile/play', methods=['GET'])
def mobile_play():
    radio_player.play()

    return redirect(session['last_url'])

# ---> Next

@mobile.route('/mobile/next', methods=['GET'])
def mobile_next():
    radio_player.next()

    return redirect(session['last_url'])


# ---> Next

@mobile.route('/mobile/previous', methods=['GET'])
def mobile_previous():
    radio_player.previous()

    return redirect(session['last_url'])


# ---> Play Pos

@mobile.route('/mobile/play_pos/<pos>', methods=['GET'])
def mobile_play_pos(pos):
    radio_player.play_song(pos)

    return redirect(session['last_url'])



###########################################################################################
# Mobile FAV
###########################################################################################

@mobile.route('/mobile/favorite', methods=['GET'])
def mobile_favorite():

    radio_list = Radios.query.filter(Radios.fav==True).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()
    artist_list = Artist.query.filter(Artist.fav==True).all()

    return render_template('mobile_favorite.html',radio_player=radio_player, radio_list=radio_list, artist_list=artist_list)


# ---> FAV

@mobile.route('/mobile/fav', methods=['GET'])
def mobile_fav():

    if radio_player.loaded == 'radio':
        radio = Radios.query.filter_by(id=radio_player.radio.id).first()

        radio.fav = not(radio.fav)

        db.session.commit()

        radio_player.radio.fav = not(radio_player.radio.fav)

    elif radio_player.loaded == 'album':

        artist = Artist.query.filter_by(id=radio_player.artist.id).first()

        artist.fav = not(artist.fav)

        db.session.commit()

        radio_player.artist.fav = not(radio_player.artist.fav)

    return redirect(session['last_url'])


###########################################################################################
# Mobile Config
###########################################################################################


# ---> Config

@mobile.route('/mobile/config', methods=['GET'])
def mobile_config():

    session['last_url'] = url_for('mobile.mobile_config')

    return render_template('mobile_config_menu.html',radio_player=radio_player)


@mobile.route('/mobile/config/server', methods=['GET'])
def mobile_config_server():

    session['last_url'] = url_for('mobile.mobile_config_server')

    return render_template('mobile_config_server.html',radio_player=radio_player)


@mobile.route('/mobile/config/outputs', methods=['GET'])
def mobile_config_outputs():

    session['last_url'] = url_for('mobile.mobile_config_outputs')

    return render_template('mobile_config_outputs.html',radio_player=radio_player)


# ---> Select Server
@mobile.route('/mobile/server/select/<hostname>', methods=['GET'])
def mobile_server_select(hostname):
    radio_player.select_server(hostname)

    return redirect(url_for('mobile.mobile_config_server'))



# ---> Toggle Output
@mobile.route('/mobile/toggle_output/<id>', methods=['GET'])
def mobile_toggle_output(id):

    radio_player.toggle_output(id)

    return redirect(url_for('mobile.mobile_config_outputs'))

