
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys

reload(sys)
sys.setdefaultencoding('utf8')

radio = Blueprint('radio', __name__)

from .models import Radios, Artist, Playlist, Podcast
from . import db, radio_player

from sqlalchemy import desc

from radio import RadioPlayer
from podcast import PodcastInfo

radio_list = Radios.query.all()

###########################################################################################
# Home
###########################################################################################

# ---> Home
@radio.route('/', methods=['GET'])
def home():

    redirect_page = 'web/playing'

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Client Home
@radio.route('/<client>', methods=['GET'])
def client_home(client):

    template_page = client + '/home.html'

    return render_template(template_page,radio_player=radio_player)

# Current Playlist
@radio.route('/<client>/playing', methods=['GET'])
def playling(client):

    if (radio_player.loaded=='album'):

        redirect_page = url_for('artist.artist_album', client=client, artist_id=radio_player.artist.id, album=radio_player.album)

    elif (radio_player.loaded=='radio'):

        redirect_page = url_for('radio.radio_show',client=client,nickname=radio_player.radio.nickname)

    elif (radio_player.loaded=='playlist'):

        redirect_page = url_for('playlist.playlist_songs_pl', client=client, pl=radio_player.playlist)

    elif (radio_player.loaded=='podcast'):

        redirect_page = url_for('podcast.podcast_episodes',client=client, id=radio_player.podcast.id)

    else:
        redirect_page = '/web/radio/all'

    session['last_url'] = redirect_page
    
    return redirect(redirect_page)

###########################################################################################
## Radio
###########################################################################################

# ----> Radio Show
@radio.route('/<client>/radio_show/<nickname>', methods=['GET'])
def radio_show(client,nickname):

    radio = Radios.query.filter_by(nickname=nickname).first()

    session['last_url'] = url_for('radio.radio_show',client=client,nickname=nickname)

    template_page = client + '/radio_show.html'

    return render_template(template_page,radio_player=radio_player,radio=radio)

# ----> Play Radio
@radio.route('/<client>/playradio/<nickname>', methods=['GET'])
def playradio(client,nickname):

    radio = Radios.query.filter_by(nickname=nickname).first()
    radio_player.playradio(radio)

    radio.num_plays = radio.num_plays + 1

    session['last_url'] = url_for('radio.radio_show',client=client,nickname=nickname)

    template_page = client + '/radio_show.html'

    return render_template(template_page,radio_player=radio_player,radio=radio)

# ----> Play Radio in Menu
@radio.route('/<client>/playradio_menu/<nickname>', methods=['GET'])
def playradio_menu(client,nickname):

    radio = Radios.query.filter_by(nickname=nickname).first()
    radio_player.playradio(radio)

    radio.num_plays = radio.num_plays + 1

    redirect_page = session['last_url']

    return redirect(redirect_page)


# Mobile Radios Menu
@radio.route('/mobile/radios', methods=['GET'])
def mobile_radios():
    return render_template('mobile/radios_menu.html')

# ---> All Radios
@radio.route('/<client>/radio/all', methods=['GET'])
def radio_all(client):
    radio_list = Radios.query.order_by(desc(Radios.num_plays)).all()
    radio_player.update_state(radio_list)

    session['last_url'] = url_for('radio.radio_all',client=client)

    template_page = client + '/radio_all.html'

    return render_template(template_page,radio_list=radio_list,radio_player=radio_player,title='All Radios')

# ---> Radio Styles
@radio.route('/<client>/radio/styles', methods=['GET'])
def radio_styles(client):

    radio_list = db.session.query(Radios.style).distinct()
    radio_styles = []
    for radio in radio_list:
        if (radio.style != ''):
            radio_styles.append(radio.style)

    session['last_url'] = url_for('radio.radio_styles',client=client)

    template_page = client + '/radio_styles.html'

    return render_template(template_page,radio_styles=radio_styles,radio_player=radio_player)

# ---> Radio Style
@radio.route('/<client>/radio/style/<style>', methods=['GET'])
def radio_style(client,style):

    radio_list = Radios.query.filter(Radios.style==style)

    session['last_url'] = url_for('radio.radio_style',client=client,style=style)

    template_page = client + '/radio_all.html'

    return render_template(template_page,radio_list=radio_list,radio_player=radio_player,title=style)

# ---> Radio Countries
@radio.route('/<client>/radio/countries', methods=['GET'])
def radio_countries(client):

    radio_list = db.session.query(Radios.country).distinct()
    radio_countries = []
    for radio in radio_list:
        if (radio.country != ''):
            radio_countries.append(radio.country)

    session['last_url'] = url_for('radio.radio_countries',client=client)

    template_page = client + '/radio_countries.html'

    return render_template(template_page,radio_countries=radio_countries,radio_player=radio_player)

# ---> Radio Country
@radio.route('/<client>/radio/country/<country>', methods=['GET'])
def radio_country(client,country):

    radio_list = Radios.query.filter(Radios.country==country)

    session['last_url'] = url_for('radio.radio_country',client=client,country=country)

    template_page = client + '/radio_all.html'

    return render_template(template_page,radio_list=radio_list,radio_player=radio_player,title=country)

# Radios List
@radio.route('/radio/list', methods=['GET'])
def radio_list():

    radio_list = Radios.query.all()

    session['last_url'] = url_for('radio.radio_list')

    return render_template('web/radio_list.html',radio_list=radio_list,radio_player=radio_player)

###########################################################################################
## Radio Add, Edit, Delete
###########################################################################################

# ---> Radio Add
@radio.route('/radio/add', methods=['GET', 'POST'])
def radio_add():

    session['last_url'] = url_for('radio.radio_add')

    return render_template('web/radio_add.html',radio_player=radio_player)

# ---> Radio Add Commit
@radio.route('/radio/add_commit', methods=['GET', 'POST'])
def radio_add_commit():

    nickname = request.form.get("nickname")
    name = request.form.get("name")
    url = request.form.get("url")
    country = request.form.get("country")
    style = request.form.get("style")
    num_plays = 0

    radio = Radios(nickname=nickname,name=name,url=url,country=country,style=style,num_plays=num_plays)

    db.session.add(radio)
    db.session.commit()

    redirect_page = url_for('radio.radio_all',client=client)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Radio Edit
@radio.route('/radio/edit/<nickname>', methods=['GET', 'POST'])
def radio_edit(nickname):
    
    radio_rec = Radios.query.filter_by(nickname=nickname).first()

    session['last_url'] = url_for('radio.radio_edit',nickname=nickname)

    return render_template('web/radio_edit.html',radio=radio_rec,radio_player=radio_player)

# ---> Radio Edit Commit
@radio.route('/radio/edit_commit/<nickname>', methods=['GET', 'POST'])
def radio_edit_commit(nickname):
    radio = Radios.query.filter_by(nickname=nickname).first()

    radio.nickname = request.form.get("nickname")
    radio.name = request.form.get("name")
    radio.url = request.form.get("url")
    radio.country = request.form.get("country")
    radio.style = request.form.get("style")
    radio.stars = request.form.get("stars")
    radio.web_url = request.form.get("web_url")
    radio.twitter = request.form.get("twitter")

    db.session.commit()

    redirect_page = url_for('radio.radio_all',client='web')

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Radio Delete
@radio.route('/radio/delete/<nickname>', methods=['GET'])
def radio_delete(nickname):
    radio = Radios.query.filter_by(nickname=nickname).first()
    db.session.delete(radio)
    db.session.commit()

    redirect_page = url_for('radio.radio_all',client='web')

    session['last_url'] = redirect_page

    return redirect(redirect_page)

