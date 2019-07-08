
from flask import render_template, redirect, request, Blueprint, session, url_for, g
import sys, os
import urllib2
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

podcast = Blueprint('podcast', __name__, template_folder='templates/podcast')

from .models import Podcast, Podcast_Link, Bookmark, Preset, Radios, Episode
from . import db, radio_player, CONFIG, download_manager
from .forms import ImageForm, LinkForm, PodcastForm, TagForm, BookmarkForm, URLForm, PodcastEpisodeForm
from .feed_manager import FeedManager

from sqlalchemy import desc

from radio import RadioPlayer
from podcast import PodcastInfo
        
###########################################################################################
# Podcast List and Load
###########################################################################################

# ---> Podcast List
@podcast.route('/podcast/list', methods=['GET'])
def podcast_list():

    podcast_list = Podcast.query.all()

    session['last_url'] = url_for('podcast.podcast_list')

    template_page = 'podcast_list.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player)

# ---> All Podcasts
@podcast.route('/podcast/all', methods=['GET'])
def podcast_all():

    podcast_list = Podcast.query.order_by(desc(Podcast.stars), Podcast.priority).all()

    session['last_url'] = url_for('podcast.podcast_all')

    template_page = 'podcast_grid.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player, title='All Podcasts')

# ---> Favorite Podcasts
@podcast.route('/podcast/favorite', methods=['GET'])
def podcast_favorite():

    podcast_list = Podcast.query.filter(Podcast.fav==True).order_by(Podcast.priority).all()

    session['last_url'] = url_for('podcast.podcast_all')

    template_page = 'podcast_grid.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player, title='Favorite Podcasts')

# ---> Styles
@podcast.route('/podcast/styles', methods=['GET'])
def podcast_styles():

    podcast_list = db.session.query(Podcast.style).distinct()
    podcast_styles = [ podcast.style for podcast in podcast_list if podcast.style != '' ]
    podcast_styles.sort()

    session['last_url'] = url_for('podcast.podcast_styles')

    template_page = 'podcast_styles.html'

    return render_template(template_page, podcast_styles=podcast_styles, radio_player=radio_player)

@podcast.route('/podcast/style/<style>', methods=['GET'])
def podcast_style(style):

    podcast_list = Podcast.query.filter(Podcast.style==style)

    session['last_url'] = url_for('podcast.podcast_style', style=style)

    template_page = 'podcast_grid.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player, title=style)

# ---> Countries
@podcast.route('/podcast/countries', methods=['GET'])
def podcast_countries():

    podcast_list = db.session.query(Podcast.country).distinct()
    podcast_countries = [ podcast.country for podcast in podcast_list if podcast.country != '' ]
    podcast_countries.sort()

    session['last_url'] = url_for('podcast.podcast_countries')

    template_page = 'podcast_countries.html'

    return render_template(template_page,podcast_countries=podcast_countries,radio_player=radio_player)

@podcast.route('/podcast/country/<country>', methods=['GET'])
def podcast_country(country):

    podcast_list = Podcast.query.filter(Podcast.country==country)

    session['last_url'] = url_for('podcast.podcast_country',country=country)

    template_page = 'podcast_grid.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player, title=country)

###########################################################################################
# Feeds, Episodes
###########################################################################################

# ---> Podcast Show
@podcast.route('/podcast/show/<id>', methods=['GET'])
def podcast_show(id):

    podcast = Podcast.query.filter_by(id=id).first()

    podcast.episode_list.sort(key=lambda x: x.pub_date, reverse=True)

    playlist = podcast.playlist

    songs_list = radio_player.playlist_songs(playlist)

    session['last_url'] = url_for('podcast.podcast_show', id=id)

    template_page = 'podcast_show.html'

    return render_template(template_page,podcast=podcast,songs_list=songs_list,radio_player=radio_player, social_sites=CONFIG.SOCIAL_SITES)


# ---> Podcast Load
@podcast.route('/podcast/load/<id>', methods=['GET'])
def podcast_load(id):

    podcast = Podcast.query.filter_by(id=id).first()

    songs_list = radio_player.playlist_songs(podcast.playlist)

    radio_player.load_podcast(podcast)

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Podcast Play Track
@podcast.route('/podcast/play_track/<id>/<track_num>', methods=['GET'])
def podcast_play_track(id,track_num):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    ep_url = pod_info.episode_url(track_num)

    radio_player.play_podcast_url(podcast,ep_url)

    redirect_page = session['last_url']

    return redirect(redirect_page)


# ---> Episode Play
@podcast.route('/podcast/episode/play/<id>', methods=['GET'])
def podcast_episode_play(id):

    episode = Episode.query.filter_by(id=id).first()

    radio_player.play_episode_url(episode)

    redirect_page = session['last_url']

    return redirect(redirect_page)

# ---> Feed Update
@podcast.route('/podcast/feed/update/<id>', methods=['GET'])
def podcast_feed_update(id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.update_feed()
    
    redirect_page = url_for('podcast.podcast_feed_episodes', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Upload Feed to Server
@podcast.route('/podcast/feed/upload_to_server/<id>', methods=['GET'])
def podcast_feed_upload_to_server(id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.upload_feed_to_server()
    
    redirect_page = url_for('podcast.podcast_feed_episodes', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Upload Image to Server
@podcast.route('/podcast/feed/upload_image_to_server/<id>', methods=['GET'])
def podcast_feed_upload_image_to_server(id):
    
    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.upload_image_to_server()
    
    redirect_page = url_for('podcast.podcast_feed_episodes', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Feed Episodes
@podcast.route('/podcast/feed/episodes/<id>', methods=['GET'])
def podcast_feed_episodes(id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.update_items_list()
    
    episodes_list = pod_info.episode_list()
    episodes_list.sort(key=lambda x: x['pubdate'], reverse=True)

    session['last_url'] = url_for('podcast.podcast_feed_episodes', id=id)

    template_page = 'podcast_feed_episodes.html'

    return render_template(template_page,podcast=podcast,episodes_list=episodes_list, radio_player=radio_player, social_sites=CONFIG.SOCIAL_SITES)


# ---> Download Episodes
@podcast.route('/podcast/download/episode/<id>/<track_num>', methods=['GET'])
def podcast_download_episode(id,track_num):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)    
    pod_info.download_episode(track_num)

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Download Episodes Statuss
@podcast.route('/podcast/download/episode/status', methods=['GET'])
def podcast_download_episode_status():

    template_page = 'podcast_episode_down_status.html'

    return render_template(template_page, radio_player=radio_player, download_manager = download_manager)

# ---> Add Episode
@podcast.route('/podcast/add_episode/<id>', methods=['GET', 'POST'])
def podcast_add_episode(id):

    form = URLForm()
    
    if form.validate_on_submit():

        name = form.name.data
        url = form.url.data

        podcast = Podcast.query.filter_by(id=id).first()
        pod_info = PodcastInfo(podcast)

        if 'temp_file' in session:
            del session['temp_file']

        if 'file_size' in session:
            del session['file_size']

        pod_info.download_episode_from_url(url,name)

        redirect_page = url_for('podcast.podcast_show',id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    session['last_url'] = url_for('podcast.podcast_add_episode',id=id)

    template_page = 'podcast_add_episode.html'

    return render_template(template_page, form=form, radio_player=radio_player, config=CONFIG)


# ---> Clear Feed
@podcast.route('/podcast/clear_feed/<id>', methods=['GET'])
def podcast_clear_feed(id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.clear_feed()

    return redirect( url_for('podcast.podcast_feed_episodes',id=id) )


# ---> Add URL to local feed
@podcast.route('/podcast/add_to_feed/<id>', methods=['GET', 'POST'])
def podcast_add_to_feed(id):

    form = PodcastEpisodeForm()
    
    if form.validate_on_submit():

        title = form.title.data
        url = form.url.data
        date = form.date.data

        podcast = Podcast.query.filter_by(id=id).first()
        pod_info = PodcastInfo(podcast)

        pod_info.add_episode_to_feed(title, url, date)

        redirect_page = url_for('podcast.podcast_feed_episodes',id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.title.data = session['feed_title']
    form.url.data = session['feed_url']
    form.date.data = session['feed_date']

    session['last_url'] = url_for('podcast.podcast_add_to_feed',id=id)

    template_page = 'podcast_add_to_feed.html'

    return render_template(template_page, form=form, radio_player=radio_player, config=CONFIG)


# ---> Import Feed from URL
@podcast.route('/podcast/import_from_url/<id>', methods=['GET','POST'])
def podcast_import_from_url(id):

    form = URLForm()

    if form.validate_on_submit():

        url = form.url.data

        feed_manager = FeedManager(url)

        session['feed_title'] = feed_manager.get_title()
        session['feed_url'] = feed_manager.get_audio_url()
        session['feed_date'] = feed_manager.get_pub_date()

        return redirect( url_for('podcast.podcast_add_to_feed', id=id) )

    else:

        return render_template('podcast_import_from_url.html', form=form, radio_player=radio_player)


# ---> Delete Episode
@podcast.route('/podcast/delete_episode/<id>/<track>', methods=['GET', 'POST'])
def podcast_delete_episode(id,track):
    
    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    pod_info.delete_episode(int(track))

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> List to Move Episode
@podcast.route('/podcast/list_to_move/episode/<src_id>/<track>', methods=['GET'])
def podcast_list_to_move_episode(src_id,track):

    podcast_list = Podcast.query.all()

    session['last_url'] = url_for('podcast.podcast_list_to_move_episode', src_id=src_id, track=track)

    template_page = 'podcast_list_to_move.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player, src_id=src_id, track=track)


# ---> Move Episode
@podcast.route('/podcast/move/episode/<src_id>/<track>/<dst_id>', methods=['GET'])
def podcast_move_episode(src_id,track,dst_id):

    src_podcast = Podcast.query.filter_by(id=src_id).first()
    src_pod_info = PodcastInfo(src_podcast)

    src_pod_info.update_items_list()
    episode_info = src_pod_info.episode_list()[int(track) - 1]

    title = episode_info['title']
    url = episode_info['url']
    date = episode_info['pubdate']
    description = episode_info['description']

    dst_podcast = Podcast.query.filter_by(id=dst_id).first()
    dst_pod_info = PodcastInfo(dst_podcast)

    dst_pod_info.add_episode_to_feed(title, url, date, description)

    return redirect(url_for('podcast.podcast_feed_episodes',id=dst_id))


# ---> Add to Preset 20
@podcast.route('/podcast/add_to_preset20/<id>/<track>', methods=['GET'])
def podcast_add_to_preset20(id,track):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    pod_info.update_items_list()
    episode_info = pod_info.episode_list()[int(track) - 1]

    title = episode_info['title']
    url = episode_info['url']

    preset = Preset.query.filter_by(id=20).first()
    radio = Radios.query.filter_by(name='Preset20').first()

    preset.url = url
    preset.name = title
    preset.radios = radio

    db.session.commit()

    return redirect(url_for('podcast.podcast_feed_episodes',id=id))


###########################################################################################
# Podcast Add, Edit, Del
###########################################################################################

# ---> Podcast Add
@podcast.route('/podcast/add', methods=['GET', 'POST'])
def podcast_add():

    form = PodcastForm()
    
    if form.validate_on_submit():

        name = form.name.data
        image = form.image.data
        playlist = form.playlist.data
        pod_dir = form.pod_dir.data

        stars = 1
        fav = False
        retag = False

        podcast = Podcast(name=name,
                        image=image,
                        playlist=playlist,
                        pod_dir=pod_dir,
                        stars=stars,
                        fav=fav,
                        retag=retag)

        db.session.add(podcast)
        db.session.commit()

        pod_info = PodcastInfo(podcast)
        pod_info.create_init_files()

        redirect_page = url_for('podcast.podcast_show',id=podcast.id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    session['last_url'] = url_for('podcast.podcast_add')

    template_page = 'podcast_add.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Podcast Edit
@podcast.route('/podcast/edit/<id>', methods=['GET', 'POST'])
def podcast_edit(id):

    podcast = Podcast.query.filter_by(id=id).first()

    form = PodcastForm()
    
    if form.validate_on_submit():

        podcast.name = form.name.data
        podcast.image = form.image.data
        podcast.playlist = form.playlist.data
        podcast.country = form.country.data
        podcast.description = form.description.data
        podcast.style = form.style.data
        podcast.feed_url = form.feed_url.data
        podcast.pod_dir = form.pod_dir.data
        podcast.feed_filter = form.feed_filter.data
        podcast.publisher = form.publisher.data
        podcast.priority = form.priority.data
        podcast.retag = form.retag.data

        db.session.commit()

        redirect_page = url_for('podcast.podcast_show',id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)


    form.name.data = podcast.name
    form.image.data = podcast.image 
    form.playlist.data = podcast.playlist
    form.country.data = podcast.country
    form.description.data = podcast.description 
    form.style.data = podcast.style 
    form.feed_url.data = podcast.feed_url 
    form.pod_dir.data = podcast.pod_dir 
    form.feed_filter.data = podcast.feed_filter 
    form.publisher.data = podcast.publisher 
    form.priority.data = podcast.priority 
    form.retag.data = podcast.retag 

    session['last_url'] = url_for('podcast.podcast_edit',id=id)

    template_page = 'podcast_edit.html'

    return render_template(template_page,form=form,radio_player=radio_player)


# ---> Podcast Delete
@podcast.route('/podcast/delete/<id>', methods=['GET'])
def podcast_delete(id):
    podcast = Podcast.query.filter_by(id=id).first()
    db.session.delete(podcast)
    db.session.commit()

    redirect_page = url_for('podcast.podcast_all')

    session['last_url'] = redirect_page

    return redirect(redirect_page)

###########################################################################################
# Episode
###########################################################################################

# ---> Episode List
@podcast.route('/podcast/episode/list/<id>', methods=['GET'])
def podcast_episode_list(id):

    podcast = Podcast.query.filter_by(id=id).first()

    episode_list = Episode.query.filter_by(podcast_id=id).order_by(desc(Episode.pub_date)).all()

    session['last_url'] = url_for('podcast.podcast_feed_episodes', id=id)

    return render_template('podcast_episode_list.html', podcast=podcast, episode_list=episode_list, radio_player=radio_player, social_sites=CONFIG.SOCIAL_SITES)


# ---> Import Episode from URL
@podcast.route('/podcast/episode/import_from_url/<id>', methods=['GET','POST'])
def podcast_episode_import_from_url(id):

    form = URLForm()

    if form.validate_on_submit():

        url = form.url.data

        feed_manager = FeedManager(url)

        session['feed_title'] = feed_manager.get_title()
        session['feed_url'] = feed_manager.get_audio_url()
        session['feed_date'] = feed_manager.get_pub_date()
        session['feed_description'] = feed_manager.get_description()
        session['feed_audio_size'] = 0

        return redirect( url_for('podcast.podcast_episode_add', id=id) )

    else:

        return render_template('podcast_import_from_url.html', form=form, radio_player=radio_player)


# ---> Add Episode to Podcast
@podcast.route('/podcast/episode/add/<id>', methods=['GET', 'POST'])
def podcast_episode_add(id):

    form = PodcastEpisodeForm()
    
    if form.validate_on_submit():

        title = form.title.data
        url = form.url.data
        date = form.date.data
        description = form.description.data
        audio_size = form.audio_size.data

        podcast = Podcast.query.filter_by(id=id).first()

        episode = Episode(title=title,
                        url=url,
                        description=description,
                        pub_date=date,
                        downloaded=False,
                        local_file='',
                        audio_size=audio_size,
                        podcast=podcast)

        db.session.add(episode)
        db.session.commit()

        redirect_page = url_for('podcast.podcast_episode_list',id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.title.data = session['feed_title']
    form.url.data = session['feed_url']
    form.date.data = session['feed_date']
    form.description.data = session['feed_description']
    form.audio_size.data = session['feed_audio_size']

    session['last_url'] = url_for('podcast.podcast_episode_add',id=id)

    template_page = 'podcast_episode_add.html'

    return render_template(template_page, form=form, radio_player=radio_player, config=CONFIG)



# ---> Edit Episode
@podcast.route('/podcast/episode/edit/<id>', methods=['GET', 'POST'])
def podcast_episode_edit(id):

    form = PodcastEpisodeForm()
    
    episode = Episode.query.filter_by(id=id).first()

    if form.validate_on_submit():

        episode.title = form.title.data
        episode.url = form.url.data
        episode.pub_date = form.date.data
        episode.description = form.description.data
        episode.audio_size = form.audio_size.data
        episode.downloaded = form.downloaded.data
        episode.local_file = form.local_file.data

        db.session.commit()

        redirect_page = url_for('podcast.podcast_episode_list',id=episode.podcast_id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.title.data = episode.title
    form.url.data = episode.url
    form.date.data = episode.pub_date
    form.description.data = episode.description
    form.audio_size.data = episode.audio_size
    form.downloaded.data = episode.downloaded
    form.local_file.data = episode.local_file

    session['last_url'] = url_for('podcast.podcast_episode_add',id=id)

    template_page = 'podcast_episode_add.html'

    return render_template(template_page, form=form, radio_player=radio_player, config=CONFIG)


# ---> Episode Delete
@podcast.route('/podcast/episode/delete/<id>', methods=['GET'])
def podcast_episode_delete(id):
    episode = Episode.query.filter_by(id=id).first()
    pod_id = episode.podcast_id
    db.session.delete(episode)
    db.session.commit()

    redirect_page = url_for('podcast.podcast_episode_list',id=pod_id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Download Episodes
@podcast.route('/podcast/episode/download/<pod_id>/<ep_id>', methods=['GET'])
def podcast_episode_download(pod_id,ep_id):

    podcast = Podcast.query.filter_by(id=pod_id).first()
    episode = Episode.query.filter_by(id=ep_id).first()

    pod_info = PodcastInfo(podcast)
    episode_data = pod_info.download_episode_file(episode)
    
    episode.local_file = episode_data['local_file']
    episode.audio_size = episode_data['file_size']
    episode.downloaded = True

    db.session.commit()

    redirect_page = url_for('podcast.podcast_show', id=pod_id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Delete Episode File
@podcast.route('/podcast/episode/delete_file/<ep_id>', methods=['GET', 'POST'])
def podcast_episode_delete_file(ep_id):
    
    episode = Episode.query.filter_by(id=ep_id).first()
    podcast = episode.podcast

    pod_info = PodcastInfo(podcast)

    pod_info.delete_episode_file(episode)

    episode.local_file = ''
    episode.downloaded = False

    db.session.commit()

    redirect_page = url_for('podcast.podcast_show', id=podcast.id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Play Episode
@podcast.route('/podcast/episode/play_local/<ep_id>', methods=['GET'])
def podcast_episode_play_local(ep_id):

    episode = Episode.query.filter_by(id=ep_id).first()

    radio_player.play_episode_file(episode)

    return redirect(session['last_url'])

# ---> Copy Episode
@podcast.route('/podcast/episode/copy/<src_id>/<track>/<dst_id>', methods=['GET'])
def podcast_episode_copy(src_id,track,dst_id):

    src_podcast = Podcast.query.filter_by(id=src_id).first()
    src_pod_info = PodcastInfo(src_podcast)

    src_pod_info.update_items_list()
    episode_info = src_pod_info.episode_list()[int(track) - 1]

    title = episode_info['title']
    url = episode_info['url']
    pub_date = episode_info['pubdate'].split(' +')[0]
    pub_date = datetime.datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S")
    pub_date = pub_date.strftime('%Y.%m.%d-%H:%M:%S')
    description = episode_info['description']
    length = episode_info['length']


    episode = Episode(title=title,
        url=url,
        description=description,
        pub_date=pub_date,
        downloaded=False,
        local_file='',
        audio_size=length,
        podcast_id=dst_id
    )

    db.session.add(episode)
    db.session.commit()

    return redirect(url_for('podcast.podcast_feed_episodes',id=dst_id))


# ---> Add Episode to DB
@podcast.route('/podcast/episode/add_to_db/<pod_id>/<track>', methods=['GET'])
def podcast_episode_add_to_db(pod_id,track):

    podcast = Podcast.query.filter_by(id=pod_id).first()
    pod_info = PodcastInfo(podcast)

    pod_info.update_items_list()
    episode_info = pod_info.episode_list()[int(track) - 1]

    title = episode_info['title']
    url = episode_info['url']
    pub_date = episode_info['pubdate'].split(' +')[0]
    pub_date = datetime.datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S")
    pub_date = pub_date.strftime('%Y.%m.%d-%H:%M:%S')
    description = episode_info['description']
    length = episode_info['length']

    urls_in_db = [ ep.url for ep in podcast.episode_list ]
    if not (url in urls_in_db):
        episode = Episode(title=title,
            url=url,
            description=description,
            pub_date=pub_date,
            downloaded=False,
            local_file='',
            audio_size=length,
            podcast_id=pod_id
        )

        db.session.add(episode)
        db.session.commit()

    return redirect(url_for('podcast.podcast_episode_list',id=pod_id))

# ---> Add to Preset 20
@podcast.route('/podcast/episode/add_to_preset20/<id>', methods=['GET'])
def podcast_episode_add_to_preset20(id):

    episode = Episode.query.filter_by(id=id).first()

    title = episode.title
    url = episode.url

    preset = Preset.query.filter_by(id=20).first()
    radio = Radios.query.filter_by(name='Preset20').first()

    preset.url = url
    preset.name = title
    preset.radios = radio

    db.session.commit()

    return redirect(url_for('podcast.podcast_episode_list',id=episode.podcast.id))


# ---> Create Feed
@podcast.route('/podcast/create_feed/<id>', methods=['GET'])
def podcast_create_feed(id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.create_feed()
    
    redirect_page = url_for('podcast.podcast_episode_list', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

###########################################################################################
# Tag Edit
###########################################################################################

# ---> Podcast Edit Tag
@podcast.route('/podcast/edit_tag/<id>/<track>', methods=['GET', 'POST'])
def podcast_edit_tag(id,track):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    [title, artist] = pod_info.file_tags(int(track))

    form = TagForm()

    if form.validate_on_submit():

        title = form.title.data

        pod_info.write_file_tags(int(track),title)

        redirect_page = url_for('podcast.podcast_show', id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)


    form.title.data = title

    session['last_url'] = url_for('podcast.podcast_edit_tag',id=id,track=track)

    return render_template('podcast_edit_tag.html',form=form,radio_player=radio_player)


# ---> Podcast Edit Tag
@podcast.route('/podcast/episode/edit_tag/<ep_id>', methods=['GET', 'POST'])
def podcast_episode_edit_tag(ep_id):

    episode = Episode.query.filter_by(id=ep_id).first()
    podcast = episode.podcast

    pod_info = PodcastInfo(podcast)
    [title, artist] = pod_info.episode_file_tags(episode)

    form = TagForm()

    if form.validate_on_submit():

        title = form.title.data

        pod_info.write_episode_file_tags(episode, title)

        redirect_page = url_for('podcast.podcast_show', id=podcast.id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)


    form.title.data = title

    session['last_url'] = url_for('podcast.podcast_episode_edit_tag',pod_id=podcast.id,ep_id=ep_id)

    return render_template('podcast_edit_tag.html',form=form,radio_player=radio_player)

###########################################################################################
# Podcast Link Add, Edit, Del
###########################################################################################

# ---> Podcast Link Add
@podcast.route('/podcast/add_link/<id>', methods=['GET', 'POST'])
def podcast_add_link(id):

    form = LinkForm()

    if form.validate_on_submit():

        name = form.name.data
        social_name = form.social_name.data
        url = form.url.data

        if social_name != 'none':
            name = social_name

        podcast = Podcast.query.filter_by(id=id).first()
        
        podcast_link = Podcast_Link(name=name,url=url,podcast=podcast)

        db.session.add(podcast_link)
        db.session.commit()

        redirect_page = url_for('podcast.podcast_show', id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)


    session['last_url'] = url_for('podcast.podcast_add_link', id=id)

    template_page = 'podcast_add_link.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Podcast Link Edit
@podcast.route('/podcast/edit_link/<id>', methods=['GET', 'POST'])
def podcast_edit_link(id):

    podcast_link = Podcast_Link.query.filter_by(id=id).first()

    form = LinkForm()

    if form.validate_on_submit():

        podcast_link.name = form.name.data
        podcast_link.url = form.url.data

        db.session.commit()

        redirect_page = url_for('podcast.podcast_show', id=podcast_link.podcast_id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = podcast_link.name
    form.url.data = podcast_link.url

    session['last_url'] = url_for('podcast.podcast_edit_link',id=id)

    template_page = 'podcast_edit_link.html'

    return render_template(template_page, form=form, radio_player=radio_player)



# ---> Delete Podcast Link
@podcast.route('/podcast/delete_link/<id>', methods=['GET', 'POST'])
def podcast_delete_link(id):

    podcast_link = Podcast_Link.query.filter_by(id=id).first()
    db.session.delete(podcast_link)
    db.session.commit()

    redirect_page = url_for('podcast.podcast_show',id=podcast_link.podcast_id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


###########################################################################################
## Fav, Unfav, Stars
###########################################################################################

# ---> Podcast Fav
@podcast.route('/podcast_fav/<id>', methods=['GET'])
def podcast_fav(id):
    podcast = Podcast.query.filter_by(id=id).first()

    podcast.fav = True

    db.session.commit()

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Podcast UnFav
@podcast.route('/podcast_unfav/<id>', methods=['GET'])
def podcast_unfav(id):
    podcast = Podcast.query.filter_by(id=id).first()

    podcast.fav = False

    db.session.commit()

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Podcast Bookmark
@podcast.route('/podcast_bookmark/<id>', methods=['GET'])
def podcast_bookmark(id):
    podcast = Podcast.query.filter_by(id=id).first()

    bookmark_url_list = [ bookmark.url for bookmark in radio_player.bookmark_list ]

    url = url_for('podcast.podcast_show',id=id)
    image_url = '/static/images/playlists/' + podcast.image
    priority = len(bookmark_url_list) + 1

    if not(url in bookmark_url_list):

        bookmark = Bookmark(url=url,
                            image_url=image_url,
                            priority=priority)

        db.session.add(bookmark)
        db.session.commit()

        radio_player.update_bookmarks()

    else:
        bookmark = Bookmark.query.filter_by(url=url).first()

        session['last_url'] = url_for('podcast.podcast_show', id=id)

        redirect_page = url_for('base.bookmark_delete',id=bookmark.id)

        return redirect(redirect_page)


    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Podcast Set Stars
@podcast.route('/podcast/stars/<id>/<stars>', methods=['GET'])
def podcast_stars(id,stars):
    podcast = Podcast.query.filter_by(id=id).first()

    podcast.stars = int(stars)

    db.session.commit()

    redirect_page = url_for('podcast.podcast_show',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Podcast External URL
@podcast.route('/podcast/episode_url/<id>/<track_num>', methods=['GET'])
def podcast_episode_url(id,track_num):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    ext_url = pod_info.episode_ext_url(int(track_num))

    return redirect(ext_url)

