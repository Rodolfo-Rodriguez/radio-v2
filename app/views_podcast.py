
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys

reload(sys)
sys.setdefaultencoding('utf8')

podcast = Blueprint('podcast', __name__)

from .models import Podcast
from . import db, radio_player

from sqlalchemy import desc

from radio import RadioPlayer
from podcast import PodcastInfo

###########################################################################################
# Podcast
###########################################################################################

# ---> All Podcasts
@podcast.route('/<client>/podcast/all', methods=['GET'])
def podcast_all(client):

    podcast_list = Podcast.query.order_by(Podcast.priority).all()

    session['last_url'] = url_for('podcast.podcast_all',client=client)

    template_page = client + '/podcast_all.html'

    return render_template(template_page,podcast_list=podcast_list,radio_player=radio_player,title='All Podcasts')


# ---> Styles
@podcast.route('/<client>/podcast/styles', methods=['GET'])
def podcast_styles(client):

    podcast_list = db.session.query(Podcast.style).distinct()
    podcast_styles = []
    for podcast in podcast_list:
        if (podcast.style != ''):
            podcast_styles.append(podcast.style)

    session['last_url'] = url_for('podcast.podcast_styles',client=client)

    template_page = client + '/podcast_styles.html'

    return render_template(template_page,podcast_styles=podcast_styles,radio_player=radio_player)

# ---> Style
@podcast.route('/<client>/podcast/style/<style>', methods=['GET'])
def podcast_style(client,style):

    podcast_list = Podcast.query.filter(Podcast.style==style)

    session['last_url'] = url_for('podcast.podcast_style',client=client,style=style)

    template_page = client + '/podcast_all.html'

    return render_template(template_page,podcast_list=podcast_list,radio_player=radio_player,title=style)


# ---> Countries
@podcast.route('/<client>/podcast/countries', methods=['GET'])
def podcast_countries(client):

    podcast_list = db.session.query(Podcast.country).distinct()
    podcast_countries = []
    for podcast in podcast_list:
        if (podcast.country != ''):
            podcast_countries.append(podcast.country)

    session['last_url'] = url_for('podcast.podcast_countries',client=client)

    template_page = client + '/podcast_countries.html'

    return render_template(template_page,podcast_countries=podcast_countries,radio_player=radio_player)

# ---> Country
@podcast.route('/<client>/podcast/country/<country>', methods=['GET'])
def podcast_country(client,country):

    podcast_list = Podcast.query.filter(Podcast.country==country)

    session['last_url'] = url_for('podcast.podcast_country',client=client,country=country)

    template_page = client + '/podcast_all.html'

    return render_template(template_page,podcast_list=podcast_list,radio_player=radio_player,title=country)

# ---> Podcast Episodes
@podcast.route('/<client>/podcast/episodes/<id>', methods=['GET'])
def podcast_episodes(client,id):

    podcast = Podcast.query.filter_by(id=id).first()

    playlist = podcast.playlist

    songs_list = radio_player.playlist_songs(playlist)

    session['last_url'] = url_for('podcast.podcast_episodes',client=client,id=id)

    template_page = client + '/podcast_episodes.html'

    return render_template(template_page,podcast=podcast,songs_list=songs_list,radio_player=radio_player)


# ---> Feed Episodes
@podcast.route('/<client>/podcast/feed/episodes/<id>', methods=['GET'])
def podcast_feed_episodes(client,id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.update_items_list()
    
    episodes_list = pod_info.episode_list()

    session['last_url'] = url_for('podcast.podcast_feed_episodes',client=client,id=id)

    template_page = client + '/podcast_feed_episodes.html'

    return render_template(template_page,podcast=podcast,episodes_list=episodes_list,radio_player=radio_player)


# ---> Download Episodes
@podcast.route('/<client>/podcast/download/episode/<id>/<track_num>', methods=['GET'])
def podcast_download_episode(client,id,track_num):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)    
    pod_info.download_episode(track_num)

    redirect_page = url_for('podcast.podcast_episodes',client=client,id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Podcast Add
@podcast.route('/podcast/add', methods=['GET', 'POST'])
def podcast_add():
    return render_template('web/podcast_add.html',radio_player=radio_player)

# ---> Podcast Add Commit
@podcast.route('/podcast/add_commit', methods=['GET', 'POST'])
def podcast_add_commit():

    name = request.form.get("name")
    image = request.form.get("image")
    playlist = request.form.get("playlist")
    pod_dir = request.form.get("pod_dir")

    podcast = Podcast(name=name,image=image,playlist=playlist,pod_dir=pod_dir)

    db.session.add(podcast)
    db.session.commit()

    pod_info = PodcastInfo(podcast)
    pod_info.create_init_files()

    return redirect('/web/podcast/all')

# ---> Podcast Edit
@podcast.route('/podcast/edit/<id>', methods=['GET'])
def podcast_edit(id):

    podcast = Podcast.query.filter_by(id=id).first()

    session['last_url'] = url_for('podcast.podcast_edit',id=id)

    return render_template('web/podcast_edit.html',podcast=podcast,radio_player=radio_player)

# ---> Podcast Edit Commit
@podcast.route('/podcast/edit_commit/<id>', methods=['GET', 'POST'])
def podcast_edit_commit(id):
    podcast = Podcast.query.filter_by(id=id).first()

    podcast.name = request.form.get("name")
    podcast.image = request.form.get("image")
    podcast.playlist = request.form.get("playlist")
    podcast.country = request.form.get("country")
    podcast.description = request.form.get("description")
    podcast.style = request.form.get("style")
    podcast.stars = request.form.get("stars")
    podcast.web_url = request.form.get("web_url")
    podcast.feed_url = request.form.get("feed_url")
    podcast.pod_dir = request.form.get("pod_dir")
    podcast.feed_filter = request.form.get("feed_filter")
    podcast.publisher = request.form.get("publisher")
    podcast.priority = request.form.get("priority")

    db.session.commit()

    redirect_page = url_for('podcast.podcast_episodes',client='web',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

@podcast.route('/podcast/delete/<id>', methods=['GET'])
def podcast_delete(id):
    podcast = Podcast.query.filter_by(id=id).first()
    db.session.delete(podcast)
    db.session.commit()

    return redirect('/web/podcast/all')


@podcast.route('/podcast/edit_tag/<id>/<track>', methods=['GET'])
def podcast_edit_tag(id,track):
    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    [title, artist] = pod_info.file_tags(int(track))

    return render_template('web/podcast_edit_tag.html',podcast=podcast,title=title,artist=artist,track=track,radio_player=radio_player)


@podcast.route('/podcast/edit_tag_commit/<id>/<track>', methods=['GET', 'POST'])
def podcast_edit_tag_commit(id,track):
    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    title = request.form.get("title")

    pod_info.write_file_tags(int(track),title)

    return redirect('/web/podcast/episodes/' + id)


@podcast.route('/<client>/podcast/load/<id>', methods=['GET'])
def podcast_load(client,id):

    podcast = Podcast.query.filter_by(id=id).first()

    songs_list = radio_player.playlist_songs(podcast.playlist)

    radio_player.load_podcast(podcast)

    template_page = client + '/podcast_episodes.html'

    return render_template(template_page,podcast=podcast,songs_list=songs_list,radio_player=radio_player)


@podcast.route('/<client>/podcast/play_song/<id>/<pos>', methods=['GET'])
def podcast_play_song(client,id,pos):

    podcast = Podcast.query.filter_by(id=id).first()

    radio_player.play_song(pos)

    songs_list = radio_player.playlist_songs(podcast.playlist)

    template_page = client + '/podcast_episodes.html'

    return render_template(template_page,podcast=podcast,songs_list=songs_list,radio_player=radio_player)


@podcast.route('/podcast/delete_episode/<id>/<track>', methods=['GET', 'POST'])
def podcast_delete_episode(id,track):
    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    pod_info.delete_episode(int(track))

    return redirect('/web/podcast/episodes/' + id)
