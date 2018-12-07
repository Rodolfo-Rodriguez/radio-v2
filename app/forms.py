from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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

class PlaylistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    playlist = StringField('Playlist', validators=[DataRequired()])
    description = StringField('Description')
    type = StringField('Type')
    submit = SubmitField('Submit')

class LinkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ArtistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image')
    image_file = FileField('Image File')
    country = StringField('Country')
    style = StringField('Style')
    description = StringField('Description')
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
    submit = SubmitField('Submit')

class TagForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
