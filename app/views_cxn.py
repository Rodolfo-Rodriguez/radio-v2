
from flask import render_template, redirect, Blueprint, session, url_for
import sys, time

reload(sys)
sys.setdefaultencoding('utf8')

cxn = Blueprint('cxn', __name__, template_folder='templates/cxn')

from . import db, radio_player, CONFIG
from .models import Preset, Radios
from .forms import RadioSearchForm

###########################################################################################
## CNX Play
###########################################################################################

@cxn.route('/cxn/radio/show', methods=['GET'])
def cxn_radio_show():

    session['last_url'] = url_for('cxn.cxn_radio_show')

    preset_id = radio_player.preset_playing
    preset = Preset.query.filter_by(id=preset_id).first()

    return render_template('cxn_radio_show.html', radio_player=radio_player, preset=preset) 


@cxn.route('/cxn/play/preset/<preset_id>', methods=['GET'])
def cxn_play_preset(preset_id):
    
    radio_player.cnx_play_preset(preset_id)
    time.sleep(4)
    radio_player.update_server_status()

    return redirect( url_for('cxn.cxn_radio_show') )


@cxn.route('/cxn/play/radio/<radio_id>', methods=['GET'])
def cxn_play_radio(radio_id):
    
    radio_player.cxn_play_radio(radio_id)   
    time.sleep(4)
    radio_player.update_server_status()

    return redirect( url_for('cxn.cxn_radio_show') )


@cxn.route('/preset20', methods=['GET'])
def cxn_preset20():
    
    preset = Preset.query.filter_by(id=20).first()

    return redirect(preset.url)


###########################################################################################
## Search
###########################################################################################

@cxn.route('/cxn/search/radio', methods=['GET','POST'])
def cxn_search_radio():

    form = RadioSearchForm()

    if form.validate_on_submit():

        name = form.name.data
        location = form.location.data

        radio_list = radio_player.cxn_search_radio(name, location)

        return render_template('cxn_list_radios.html', radio_list=radio_list, radio_player=radio_player)
    
    session['last_url'] = url_for('cxn.cxn_search_radio')

    return render_template('cxn_search_radio.html', form=form, radio_player=radio_player)


@cxn.route('/cxn/list/locations', methods=['GET'])
def cxn_list_locations():

    location_list = radio_player.cxn_locations()
    
    session['last_url'] = url_for('cxn.cxn_list_locations')

    return render_template('cxn_list_locations.html', location_list=location_list, radio_player=radio_player)


@cxn.route('/cxn/list/genres', methods=['GET'])
def cxn_list_genres():

    genre_list = radio_player.cxn_genre_list()
    
    session['last_url'] = url_for('cxn.cxn_list_genres')

    return render_template('cxn_list_genres.html', genre_list=genre_list, radio_player=radio_player)


@cxn.route('/cxn/list/radios/location/<location_id>', methods=['GET'])
def cxn_list_radios_location(location_id):

    radio_list = radio_player.list_radios_in_cxn_location(location_id)
    
    session['last_url'] = url_for('cxn.cxn_list_radios_location', location_id=location_id)

    return render_template('cxn_list_radios.html', radio_list=radio_list, radio_player=radio_player)


@cxn.route('/cxn/list/radios/genre/<genre_id>', methods=['GET'])
def cxn_list_radios_genre(genre_id):

    radio_list = radio_player.list_radios_in_cxn_genre(genre_id)
    
    session['last_url'] = url_for('cxn.cxn_list_radios_genre', genre_id=genre_id)

    return render_template('cxn_list_radios.html', radio_list=radio_list, radio_player=radio_player)


###########################################################################################
## Presets
###########################################################################################

@cxn.route('/cxn/radio/add_current_to_preset/<preset_id>', methods=['GET','POST'])
def cxn_radio_add_current_to_preset(preset_id):

    radio_list = Radios.query.all()

    return render_template('cxn_radio_add_current_to_preset.html', radio_list=radio_list, preset_id=preset_id, radio_player=radio_player)


@cxn.route('/cxn/radio/add_to_preset/<radio_id>/<preset_id>', methods=['GET'])
def cxn_radio_add_to_preset(radio_id, preset_id):

    preset = Preset.query.filter_by(id=preset_id).first()

    preset.name = radio_player.cxn_client.playback_details['title']

    preset.description = ''

    preset.url = radio_player.cxn_client.playback_details['url']

    radio = Radios.query.filter_by(id=radio_id).first()

    preset.radios = radio

    db.session.commit()

    ## Update CXN

    radio_player.preset_playing = int(preset_id)
    radio_player.cxn_set_preset(preset_id)

    return redirect( url_for('cxn.cxn_radio_show') )


@cxn.route('/cxn/server/list/presets', methods=['GET','POST'])
def cxn_server_list_preset():

    return render_template('cxn_server_list_presets.html', radio_player=radio_player)
