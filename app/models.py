
from . import db

class Radios(db.Model):
    __tablename__ = 'radios'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    url = db.Column(db.String(120),nullable=True)
    image = db.Column(db.String(120),nullable=True)
    country = db.Column(db.String(80),nullable=False)
    num_plays = db.Column(db.Integer,nullable=False)
    style = db.Column(db.String(120),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    fav = db.Column(db.Boolean,nullable=False)
    description = db.Column(db.String(120),nullable=True)
    radio_link_list = db.relationship('Radio_Link', backref='radios')
    program_list = db.relationship('Program', backref='radios')

class Program(db.Model):
    __tablename__ = 'program'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    times = db.Column(db.String(80),nullable=True)
    week_days = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    twitter = db.Column(db.String(120),nullable=True)
    radio_id = db.Column(db.Integer, db.ForeignKey('radios.id'), nullable=False)

class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False)
    country = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    artist_link_list = db.relationship('Artist_Link', backref='artist')

class Playlist(db.Model):
    __tablename__ = 'playlist'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False)
    playlist = db.Column(db.String(80),nullable=False)
    description = db.Column(db.String(120),nullable=True)
    type = db.Column(db.String(80),nullable=True)

class Podcast(db.Model):
    __tablename__ = 'podcast'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False)
    playlist = db.Column(db.String(80),nullable=False)
    country = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    feed_url = db.Column(db.String(120),nullable=True)
    feed_filter = db.Column(db.String(80),nullable=True)
    pod_dir = db.Column(db.String(120),nullable=False)
    publisher = db.Column(db.String(80),nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    retag = db.Column(db.Boolean,nullable=True)
    podcast_link_list = db.relationship('Podcast_Link', backref='podcast')

class Radio_Link(db.Model):
    __tablename__ = 'radio_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    url = db.Column(db.String(120),nullable=False)
    radio_id = db.Column(db.Integer, db.ForeignKey('radios.id'), nullable=False)

class Artist_Link(db.Model):
    __tablename__ = 'artist_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    url = db.Column(db.String(120),nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

class Podcast_Link(db.Model):
    __tablename__ = 'podcast_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    url = db.Column(db.String(120),nullable=False)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'), nullable=False)

class Bookmark(db.Model):
    __tablename__ = 'bookmark'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120),nullable=False)
    image_url = db.Column(db.String(120),nullable=False)
    priority = db.Column(db.Integer, nullable=True)

