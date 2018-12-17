
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys, os

from sqlalchemy import desc

reload(sys)
sys.setdefaultencoding('utf8')

base = Blueprint('base', __name__, template_folder='templates/base')

from . import db, radio_player, CONFIG, db_manager
from .forms import BookmarkForm

from radio import RadioPlayer, Bookmark

###########################################################################################
# Home
###########################################################################################

# ---> Home
@base.route('/', methods=['GET'])
def home():

    radio_player.disconnect()
    radio_player.update_bookmarks()

    session['last_url'] = '/'

    template_page = 'home.html'

    return render_template(template_page, radio_player=radio_player,db_manager=db_manager)

###########################################################################################
##  Playing
###########################################################################################

# ---> Current Playlist
@base.route('/playing', methods=['GET'])
def playling():

    if (radio_player.loaded=='album'):

        redirect_page = url_for('artist.artist_album', artist_id=radio_player.artist.id, album=radio_player.album)

    elif (radio_player.loaded=='radio'):

        redirect_page = url_for('radio.radio_show', id=radio_player.radio.id)

    elif (radio_player.loaded=='playlist'):

        redirect_page = url_for('playlist.playlist_show', id=radio_player.playlist.id)

    elif (radio_player.loaded=='podcast'):

        redirect_page = url_for('podcast.podcast_show', id=radio_player.podcast.id)

    elif (radio_player.loaded=='podcast-url'):

        redirect_page = url_for('podcast.podcast_show', id=radio_player.podcast.id)

    else:
        redirect_page = url_for('base.home')

    session['last_url'] = redirect_page
    
    return redirect(redirect_page)

# ---> Bookmarks List
@base.route('/bookmark/list', methods=['GET'])
def bookmark_list():

    bookmark_list = Bookmark.query.order_by(desc(Bookmark.priority)).all()

    session['last_url'] = url_for('base.bookmark_list')

    template_page = 'bookmark_list.html'

    return render_template(template_page, radio_player=radio_player,bookmark_list=bookmark_list)


# ---> Bookmark Edit
@base.route('/bookmark/edit/<id>', methods=['GET', 'POST'])
def bookmark_edit(id):

    bookmark = Bookmark.query.filter_by(id=id).first()

    form = BookmarkForm()

    if form.validate_on_submit():

        bookmark.url = form.url.data
        bookmark.image_url = form.image_url.data
        bookmark.priority = form.priority.data

        db.session.commit()

        radio_player.update_bookmarks()

        redirect_page = url_for('base.bookmark_list')

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.url.data = bookmark.url
    form.image_url.data = bookmark.image_url
    form.priority.data = bookmark.priority

    session['last_url'] = url_for('base.bookmark_edit',id=id)

    template_page = 'bookmark_edit.html'

    return render_template(template_page, form=form, radio_player=radio_player)

# ---> Bookmark Delete
@base.route('/bookmark/delete/<id>', methods=['GET'])
def bookmark_delete(id):
    bookmark = Bookmark.query.filter_by(id=id).first()

    db.session.delete(bookmark)
    db.session.commit()

    radio_player.update_bookmarks()

    redirect_page = session['last_url']

    return redirect(redirect_page)

