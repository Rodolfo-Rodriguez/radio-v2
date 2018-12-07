
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys

reload(sys)
sys.setdefaultencoding('utf8')

podcast = Blueprint('podcast', __name__, template_folder='templates/podcast')

from .models import Podcast, Podcast_Link
from . import db, radio_player, CONFIG
from .forms import ImageForm, LinkForm, PodcastForm, TagForm

from sqlalchemy import desc

from radio import RadioPlayer
from podcast import PodcastInfo

###########################################################################################
# Podcast List and Load
###########################################################################################

# ---> All Podcasts
@podcast.route('/podcast/all', methods=['GET'])
def podcast_all():

    podcast_list = Podcast.query.order_by(Podcast.priority).all()

    session['last_url'] = url_for('podcast.podcast_all')

    template_page = 'podcast_grid.html'

    return render_template(template_page, podcast_list=podcast_list, radio_player=radio_player, title='All Podcasts')

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

    session['last_url'] = url_for('podcast.podcast_show',id=id)

    template_page = 'podcast_show.html'

    return render_template(template_page,podcast=podcast,songs_list=songs_list,radio_player=radio_player, social_sites=CONFIG.SOCIAL_SITES)


# ---> Feed Episodes
@podcast.route('/podcast/feed/episodes/<id>', methods=['GET'])
def podcast_feed_episodes(id):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)
    pod_info.update_items_list()
    
    episodes_list = pod_info.episode_list()

    session['last_url'] = url_for('podcast.podcast_feed_episodes', id=id)

    template_page = 'podcast_feed_episodes.html'

    return render_template(template_page,podcast=podcast,episodes_list=episodes_list,radio_player=radio_player)


# ---> Download Episodes
@podcast.route('/podcast/download/episode/<id>/<track_num>', methods=['GET'])
def podcast_download_episode(id,track_num):

    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)    
    pod_info.download_episode(track_num)

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Delete Episode
@podcast.route('/podcast/delete_episode/<id>/<track>', methods=['GET', 'POST'])
def podcast_delete_episode(id,track):
    
    podcast = Podcast.query.filter_by(id=id).first()
    pod_info = PodcastInfo(podcast)

    pod_info.delete_episode(int(track))

    redirect_page = url_for('podcast.podcast_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


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

        podcast = Podcast(name=name,
                        image=image,
                        playlist=playlist,
                        pod_dir=pod_dir,
                        stars=stars,
                        fav=fav)

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


###########################################################################################
# Podcast Link Add, Edit, Del
###########################################################################################

# ---> Podcast Link Add
@podcast.route('/podcast/add_link/<id>', methods=['GET', 'POST'])
def podcast_add_link(id):

    form = LinkForm()

    if form.validate_on_submit():

        name = form.name.data
        url = form.url.data

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

