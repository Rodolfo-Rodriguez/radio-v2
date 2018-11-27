
from . import db

class Radios(db.Model):
    __tablename__ = 'radios'
    nickname = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    url = db.Column(db.String(120),nullable=True)
    country = db.Column(db.String(80),nullable=False)
    num_plays = db.Column(db.Integer,nullable=False)
    style = db.Column(db.String(120),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    web_url = db.Column(db.String(120),nullable=True)
    twitter = db.Column(db.String(120),nullable=True)

class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False)
    country = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)

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
    web_url = db.Column(db.String(120),nullable=True)
    feed_url = db.Column(db.String(120),nullable=True)
    feed_filter = db.Column(db.String(80),nullable=True)
    pod_dir = db.Column(db.String(120),nullable=False)
    publisher = db.Column(db.String(80),nullable=True)
    priority = db.Column(db.Integer, nullable=True)
