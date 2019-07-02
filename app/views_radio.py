
from flask import render_template, redirect, request, Blueprint, session, url_for
import sys, os, time

from sqlalchemy import desc

reload(sys)
sys.setdefaultencoding('utf8')

radio = Blueprint('radio', __name__, template_folder='templates/radio')

from . import db, radio_player, CONFIG
from .models import Radios, Program, Artist, Playlist, Podcast, Radio_Link, Bookmark, Preset
from .forms import RadioForm, ImageForm, ProgramForm, LinkForm, RadioSearchForm, PresetForm

from program_info import ProgramsInfo
from podcast import PodcastInfo


###########################################################################################
## List, Grid
###########################################################################################

# ---> Radios List
@radio.route('/radio/list', methods=['GET'])
def radio_list():

    radio_list = Radios.query.all()

    session['last_url'] = url_for('radio.radio_list')

    template_page = 'radio_list.html'

    return render_template(template_page, radio_list=radio_list, radio_player=radio_player)

# ---> All Radios
@radio.route('/radio/all', methods=['GET'])
def radio_all():
    radio_list = Radios.query.order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()
    radio_player.update_state(radio_list)

    session['last_url'] = url_for('radio.radio_all')

    template_page = 'radio_grid.html'

    return render_template(template_page,radio_list=radio_list,radio_player=radio_player,title='All Radios')

# ---> Favorite Radios
@radio.route('/radio/favorite', methods=['GET'])
def radio_favorite():
    radio_list = Radios.query.filter(Radios.fav==True).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()
    radio_player.update_state(radio_list)

    session['last_url'] = url_for('radio.radio_all')

    template_page = 'radio_grid.html'

    return render_template(template_page,radio_list=radio_list,radio_player=radio_player,title='Favorite Radios')

# ---> Radio Presets
@radio.route('/radio/presets', methods=['GET'])
def radio_presets():

    preset_list = Preset.query.all()

    session['last_url'] = url_for('radio.radio_all')

    template_page = 'radio_preset_list.html'

    return render_template(template_page,preset_list=preset_list,radio_player=radio_player,title='Presets')

# ---> Radio Styles
@radio.route('/radio/styles', methods=['GET'])
def radio_styles():

    radio_list = db.session.query(Radios.style).distinct()
    radio_styles = [ radio.style for radio in radio_list if radio.style != '']
    radio_styles.sort()

    session['last_url'] = url_for('radio.radio_styles')

    template_page = 'radio_styles.html'

    return render_template(template_page, radio_styles=radio_styles, radio_player=radio_player)

# ---> Radio Style
@radio.route('/radio/style/<style>', methods=['GET'])
def radio_style(style):

    radio_list = Radios.query.filter(Radios.style==style).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()

    session['last_url'] = url_for('radio.radio_style', style=style)

    template_page = 'radio_grid.html'

    return render_template(template_page, radio_list=radio_list, radio_player=radio_player, title=style)

# ---> Radio Countries
@radio.route('/radio/countries', methods=['GET'])
def radio_countries():

    radio_list = db.session.query(Radios.country).distinct()
    radio_countries = [ radio.country for radio in radio_list if radio.country != '' ]
    radio_countries.sort()

    session['last_url'] = url_for('radio.radio_countries')

    template_page = 'radio_countries.html'

    return render_template(template_page, radio_countries=radio_countries, radio_player=radio_player)

# ---> Radio Country
@radio.route('/radio/country/<country>', methods=['GET'])
def radio_country(country):

    radio_list = Radios.query.filter(Radios.country==country).order_by(desc(Radios.stars)).order_by(desc(Radios.num_plays)).all()

    session['last_url'] = url_for('radio.radio_country', country=country)

    template_page = 'radio_grid.html'

    return render_template(template_page, radio_list=radio_list, radio_player=radio_player, title=country)


# ---> Radio Grid
@radio.route('/radio/grid', methods=['GET'])
def radio_grid():
    radio_player.update_bookmarks()

    radio_list = Radios.query.filter(Radios.preset > 0).order_by(Radios.preset).all()

    session['last_url'] = url_for('radio.radio_grid')

    template_page = 'radio_grid_flat.html'

    return render_template(template_page, radio_list=radio_list, radio_player=radio_player, title='Presets')


# ---> Radio Presets Grid
@radio.route('/radio/grid/presets', methods=['GET'])
def radio_grid_presets():

    preset_list = Preset.query.all()

    session['last_url'] = url_for('radio.radio_grid_presets')

    template_page = 'radio_grid_presets.html'

    return render_template(template_page, preset_list=preset_list, radio_player=radio_player)

###########################################################################################
## Show, Play
###########################################################################################

# ----> Set Week Day
@radio.route('/radio/set_wday/<id>/<wday>', methods=['GET'])
def radio_set_wday(id,wday):
    
    session['list_week_day'] = int(wday)

    redirect_page = url_for('radio.radio_show',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ----> Radio Show
@radio.route('/radio_show/<id>', methods=['GET'])
def radio_show(id):

    radio = Radios.query.filter_by(id=id).first()

    programs_info = ProgramsInfo(radio)

    if 'list_week_day' in session:
        programs_info.set_list_week_day(session['list_week_day'])

    session['last_url'] = url_for('radio.radio_show',id=id)

    template_page = 'radio_show.html'

    return render_template(template_page,radio_player=radio_player,radio=radio, programs_info=programs_info, social_sites=CONFIG.SOCIAL_SITES) 

# ----> Play Radio
@radio.route('/playradio/<id>/', methods=['GET'])
def playradio(id):

    radio = Radios.query.filter_by(id=id).first()
    radio.num_plays = radio.num_plays + 1
    db.session.commit()

    radio_player.playradio(radio)
    
    if 'list_week_day' in session:
        del session['list_week_day']

    redirect_page = url_for('radio.radio_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ----> Play Radio in Menu
@radio.route('/playradio_menu/<id>', methods=['GET'])
def playradio_menu(id):

    radio = Radios.query.filter_by(id=id).first()
    preset_id = radio.preset_number()

    if radio_player.server_type == 'CXN':
        if preset_id > 0:
            radio_player.cxn_play_preset(preset_id)
            time.sleep(4)
            radio_player.update_server_status()
    else:
        radio_player.playradio(radio)
    
    if 'list_week_day' in session:
        del session['list_week_day']

    redirect_page = session['last_url']

    return redirect(redirect_page)


# ----> Play Radio Preset
@radio.route('/play/radio/preset/<id>', methods=['GET'])
def play_radio_preset(id):

    preset = Preset.query.filter_by(id=id).first()

    if radio_player.server_type == 'CXN':
        radio_player.cxn_play_preset(id)
        time.sleep(4)
        radio_player.update_server_status()

        redirect_page = url_for('cxn.cxn_radio_show')
    else:
        radio_player.playradio(preset.radios)
        redirect_page = url_for('radio.radio_show', id=preset.radio_id)

    return redirect(redirect_page)

###########################################################################################
## Radio Add, Edit, Delete
###########################################################################################

# ---> Radio Add
@radio.route('/radio/add', methods=['GET', 'POST'])
def radio_add():

    form = RadioForm()

    if form.validate_on_submit():

        name = form.name.data
        image_file = form.image_file.data
        url = form.url.data
        country = form.country.data
        style = form.style.data

        num_plays = 0
        stars = 1
        fav = False
        description = ''

        image = name + '.png'

        image_file.save(os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_RADIOS_IMG_DIR, image))

        radio = Radios(name=name,
                    url=url,
                    image=image,
                    country=country,
                    style=style,
                    num_plays=num_plays,
                    stars=stars,
                    description=description,
                    fav=fav)

        db.session.add(radio)
        db.session.commit()

        redirect_page = url_for('radio.radio_show',id=radio.id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = radio_player.server_currentsong('name')
    form.url.data = radio_player.server_currentsong('file')

    session['last_url'] = url_for('radio.radio_add')

    template_page = 'radio_add.html'

    return render_template(template_page, radio_player=radio_player, form=form)


# ---> Radio Edit
@radio.route('/radio/edit/<id>', methods=['GET', 'POST'])
def radio_edit(id):
    
    radio = Radios.query.filter_by(id=id).first()

    form = RadioForm()

    if form.validate_on_submit():

        radio.name = form.name.data
        radio.url = form.url.data
        radio.image = form.image.data
        radio.description = form.description.data
        radio.country = form.country.data
        radio.style = form.style.data

        db.session.commit()

        redirect_page = url_for('radio.radio_show',client='web',id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = radio.name
    form.url.data = radio.url
    form.image.data = radio.image 
    form.description.data = radio.description
    form.country.data = radio.country
    form.style.data = radio.style

    session['last_url'] = url_for('radio.radio_edit', id=id)

    template_page = 'radio_edit.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Radio Delete
@radio.route('/radio/delete/<id>', methods=['GET'])
def radio_delete(id):
    radio = Radios.query.filter_by(id=id).first()
    
    radio_links = Radio_Link.query.filter_by(radio_id=id).all()

    for link in radio_links:
        db.session.delete(link)

    db.session.delete(radio)

    db.session.commit()

    redirect_page = url_for('radio.radio_all',client='web')

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Edit Image
@radio.route('/radio/edit_image/<id>', methods=['GET', 'POST'])
def radio_edit_image(id):

    radio = Radios.query.filter_by(id=id).first()

    form = ImageForm()

    if form.validate_on_submit():

        image_file = form.image_file.data

        image = radio.name + '.png'

        image_file.save(os.path.join(CONFIG.PROJECT_ROOT_DIR, CONFIG.PROJECT_RADIOS_IMG_DIR, image))

        redirect_page = url_for('radio.radio_show',id=id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)


    session['last_url'] = url_for('radio.radio_edit_image',id=id)

    template_page = 'radio_edit_image.html'

    return render_template(template_page, form=form, radio_player=radio_player)

###########################################################################################
## Presets
###########################################################################################

# ---> Set to Preset 20
@radio.route('/radio/set_to_preset20/<id>', methods=['GET', 'POST'])
def radio_set_to_preset20(id):

    radio = Radios.query.filter_by(id=id).first()
    preset = Preset.query.filter_by(id=20).first()

    preset.url = radio.url
    preset.name = radio.name
    preset.radios = radio

    db.session.commit()

    return redirect(session['last_url'])


# ---> Preset Edit
@radio.route('/radio/preset/edit/<id>', methods=['GET', 'POST'])
def radio_preset_edit(id):

    preset = Preset.query.filter_by(id=id).first()

    form = PresetForm()

    if form.validate_on_submit():

        preset.name = form.name.data
        preset.description = form.description.data
        preset.url = form.url.data

        db.session.commit() 

        redirect_page = '/radio/presets'

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = preset.name
    form.description.data = preset.description
    form.url.data = preset.url

    session['last_url'] = url_for('radio.radio_preset_edit',id=id)

    template_page = 'radio_preset_edit.html'

    return render_template(template_page, form=form, radio_player=radio_player)

###########################################################################################
## Radio Link Add, Edit, Delete
###########################################################################################

# ---> Radio Link Add
@radio.route('/radio/add_link/<id>', methods=['GET', 'POST'])
def radio_add_link(id):

    form = LinkForm()

    if form.validate_on_submit():

        name = form.name.data
        social_name = form.social_name.data
        url = form.url.data

        if social_name != 'none':
            name = social_name

        radio = Radios.query.filter_by(id=id).first()

        radio_link = Radio_Link(name=name,
                                url=url,
                                radios=radio)

        db.session.add(radio_link)
        db.session.commit()

        redirect_page = url_for('radio.radio_show',id=id)
        session['last_url'] = redirect_page

        return redirect(redirect_page)

    
    session['last_url'] = url_for('radio.radio_add_link',id=id)

    template_page = 'radio_add_link.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Radio Link Edit
@radio.route('/radio/edit_link/<id>', methods=['GET', 'POST'])
def radio_edit_link(id):

    radio_link = Radio_Link.query.filter_by(id=id).first()

    form = LinkForm()

    if form.validate_on_submit():

        radio_link.name = form.name.data
        radio_link.url = form.url.data

        db.session.commit()

        redirect_page = url_for('radio.radio_show',id=radio_link.radio_id)

        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = radio_link.name
    form.url.data = radio_link.url

    session['last_url'] = url_for('radio.radio_edit_link',id=id)

    template_page = 'radio_edit_link.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Radio Link Delete
@radio.route('/radio/delete_link/<id>', methods=['GET'])
def radio_link_delete(id):
    radio_link = Radio_Link.query.filter_by(id=id).first()
    id = radio_link.radio_id

    db.session.delete(radio_link)
    db.session.commit()

    redirect_page = url_for('radio.radio_show',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

###########################################################################################
## Fav, Unfav, Bookmark, Stars
###########################################################################################

# ---> Radio Fav
@radio.route('/radio_fav/<id>', methods=['GET'])
def radio_fav(id):
    radio = Radios.query.filter_by(id=id).first()

    radio.fav = True

    db.session.commit()

    redirect_page = url_for('radio.radio_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Radio UnFav
@radio.route('/radio_unfav/<id>', methods=['GET'])
def radio_unfav(id):
    radio = Radios.query.filter_by(id=id).first()

    radio.fav = False

    db.session.commit()

    redirect_page = url_for('radio.radio_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Radio Bookmark
@radio.route('/radio_bookmark/<id>', methods=['GET'])
def radio_bookmark(id):
    radio = Radios.query.filter_by(id=id).first()

    bookmark_url_list = [ bookmark.url for bookmark in radio_player.bookmark_list ]

    url = url_for('radio.playradio_menu',id=id)
    image_url = '/static/images/radios/' + radio.image
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

        session['last_url'] = url_for('radio.radio_show', id=id)

        redirect_page = url_for('base.bookmark_delete',id=bookmark.id)

        return redirect(redirect_page)


    redirect_page = url_for('radio.radio_show', id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)

# ---> Radio Set Stars
@radio.route('/radio/stars/<id>/<stars>', methods=['GET'])
def radio_stars(id,stars):
    radio = Radios.query.filter_by(id=id).first()

    radio.stars = int(stars)

    db.session.commit()

    redirect_page = url_for('radio.radio_show',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)


# ---> Radio Set Preset
@radio.route('/radio/set_preset/<id>/<preset>', methods=['GET'])
def radio_set_preset(id,preset):
    radio_new = Radios.query.filter_by(id=id).first()

    radio_old = Radios.query.filter_by(preset=preset).first()

    if radio_old:
        radio_old.preset = 0

    radio_new.preset = int(preset)

    db.session.commit()

    redirect_page = url_for('radio.radio_show',id=id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)
###########################################################################################
## Program
###########################################################################################

# ---> Program List
@radio.route('/radio/list_program', methods=['GET'])
def radio_list_program():

    program_list = Program.query.all()

    session['last_url'] = url_for('radio.radio_list_program')

    template_page = 'radio_program_list.html'

    return render_template(template_page, program_list=program_list, radio_player=radio_player)

# ---> Program Add
@radio.route('/radio/add_program/<id>', methods=['GET', 'POST'])
def radio_add_program(id):

    form = ProgramForm()

    if form.validate_on_submit():

        name = form.name.data
        times = form.times.data
        week_days = form.week_days.data

        description = ''
        style = ''
        stars = 0
        fav = False

        radio = Radios.query.filter_by(id=id).first()

        program = Program(name=name,
                        times=times,
                        week_days=week_days,
                        description=description,
                        style=style,
                        stars=stars,
                        fav=fav,
                        radios=radio)

        db.session.add(program)
        db.session.commit()

        redirect_page = url_for('radio.radio_show',id=id)
        session['last_url'] = redirect_page

        return redirect(redirect_page)

    
    form.times.data = 'XX:00-XX:00'
    form.week_days.data = '0,1,2,3,4'

    session['last_url'] = url_for('radio.radio_add_program',id=id)

    template_page = 'radio_add_program.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Program Edit
@radio.route('/radio/edit_program/<id>', methods=['GET', 'POST'])
def radio_edit_program(id):

    program = Program.query.filter_by(id=id).first()
 
    form = ProgramForm()

    if form.validate_on_submit():

        program.name = form.name.data
        program.times = form.times.data
        program.week_days = form.week_days.data
        program.description = form.description.data
        program.style = form.style.data
        program.twitter = form.twitter.data

        db.session.commit()

        redirect_page = url_for('radio.radio_show',id=program.radio_id)
        session['last_url'] = redirect_page

        return redirect(redirect_page)

    form.name.data = program.name
    form.times.data = program.times
    form.week_days.data = program.week_days
    form.description.data = program.description
    form.style.data = program.style
    form.twitter.data = program.twitter
    
    session['last_url'] = url_for('radio.radio_edit_program',id=id)

    template_page = 'radio_edit_program.html'

    return render_template(template_page, form=form, radio_player=radio_player)


# ---> Program Delete
@radio.route('/radio/delete_program/<id>', methods=['GET'])
def radio_program_delete(id):
    program = Program.query.filter_by(id=id).first()
    radio_id = program.radio_id

    db.session.delete(program)
    db.session.commit()

    redirect_page = url_for('radio.radio_show',id=radio_id)

    session['last_url'] = redirect_page

    return redirect(redirect_page)
