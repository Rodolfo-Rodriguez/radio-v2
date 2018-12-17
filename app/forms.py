from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class RadioForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image')
    image_file = FileField('Image File')
    url = StringField('URL', validators=[DataRequired()])
    country = StringField('Country')
    style = StringField('Style')
    description = StringField('Description')
    submit = SubmitField('Submit')

class ImageForm(FlaskForm):
    image_file = FileField('Image File',validators=[FileRequired()])
    submit = SubmitField('Submit')

class ProgramForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    times = StringField('Times')
    week_days = StringField('Week Days')
    description = StringField('Description')
    country = StringField('Country')
    style = StringField('Style')
    twitter = StringField('Twitter')
    submit = SubmitField('Submit')

class ArtistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image')
    image_file = FileField('Image File')
    country = StringField('Country')
    style = StringField('Style')
    description = StringField('Description')
    submit = SubmitField('Submit')

class PlaylistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    playlist = StringField('Playlist', validators=[DataRequired()])
    description = StringField('Description')
    type = StringField('Type')
    submit = SubmitField('Submit')

class LinkForm(FlaskForm):
    name = StringField('Name')
    social_name = SelectField('Social', choices=[('none', 'none'), 
                                                ('twitter', 'Twitter'), 
                                                ('instagram', 'Instagram'),
                                                ('youtube','Youtube'),
                                                ('spotify','Spotify'),
                                                ('apple','Apple Music'),
                                                ('soundcloud','Soundcloud')])
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PodcastForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image')
    image_file = FileField('Image File')
    playlist = StringField('Playlist', validators=[DataRequired()])
    pod_dir = StringField('Pod Dir', validators=[DataRequired()])
    feed_url = StringField('Feed URL')
    feed_filter = StringField('Feed Filename Filter')
    country = StringField('Country')
    style = StringField('Style')
    publisher = StringField('Publisher')
    description = StringField('Description')
    priority = StringField('Priority')
    stars = StringField('Stars')
    retag = BooleanField('Add Date to Tag')
    submit = SubmitField('Submit')

class TagForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class URLForm(FlaskForm):
    name = StringField('Name')
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BookmarkForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    image_url = StringField('URL', validators=[DataRequired()])
    priority = StringField('Priority')
    submit = SubmitField('Submit')
