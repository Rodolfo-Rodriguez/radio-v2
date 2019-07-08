
from . import db
import datetime

##################################################################################################
# Radios
##################################################################################################
class Radios(db.Model):
    __tablename__ = 'radios'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    url = db.Column(db.String(120),nullable=True)
    image = db.Column(db.String(120),nullable=True)
    country = db.Column(db.String(80),nullable=True)
    num_plays = db.Column(db.Integer,nullable=True)
    style = db.Column(db.String(120),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    description = db.Column(db.String(120),nullable=True)
    radio_link_list = db.relationship('Radio_Link', backref='radios')
    program_list = db.relationship('Program', backref='radios')
    preset_list = db.relationship('Preset', backref='radios')

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.url,
            self.image,
            self.country,
            self.num_plays,
            self.style,
            self.stars,
            self.fav,
            self.description
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")
        
        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.url = words[2].decode('utf-8')
            self.image = words[3].decode('utf-8')
            self.country = words[4].decode('utf-8')
            self.num_plays = int(words[5])
            self.style = words[6].decode('utf-8')
            self.stars = int(words[7])
            self.fav = (words[8]=='True')
            self.description = words[9].decode('utf-8')

    def preset_number(self):
        if self.preset_list:
            return self.preset_list[0].id
        else:
            return 0

    def preset_name(self):
        if self.preset_list:
            return self.preset_list[0].name
        else:
            return ''

    def preset_url(self):
        if self.preset_list:
            return self.preset_list[0].url
        else:
            return ''


##################################################################################################
# Program
##################################################################################################
class Program(db.Model):
    __tablename__ = 'program'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    times = db.Column(db.String(80),nullable=True)
    week_days = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    twitter = db.Column(db.String(120),nullable=True)
    radio_id = db.Column(db.Integer, db.ForeignKey('radios.id'), nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.times,
            self.week_days,
            self.description,
            self.style,
            self.stars,
            self.fav,
            self.twitter,
            self.radio_id 
          ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.times = words[2].decode('utf-8')
            self.week_days = words[3].decode('utf-8')
            self.description = words[4].decode('utf-8')
            self.style = words[5].decode('utf-8')
            self.stars = int(words[6])
            self.fav = (words[7]=='True')
            self.twitter = words[8].decode('utf-8')
            self.radio_id = int(words[9])


##################################################################################################
# Artist
##################################################################################################
class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    image = db.Column(db.String(80),nullable=True)
    country = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    artist_link_list = db.relationship('Artist_Link', backref='artist')

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.image,
            self.country,
            self.description,
            self.style,
            self.stars,
            self.fav
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.image = words[2].decode('utf-8')
            self.country = words[3].decode('utf-8')
            self.description = words[4].decode('utf-8')
            self.style = words[5].decode('utf-8')
            self.stars = int(words[6])
            self.fav = (words[7]=='True')

##################################################################################################
# Playlist
##################################################################################################
class Playlist(db.Model):
    __tablename__ = 'playlist'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    image = db.Column(db.String(80),nullable=True)
    playlist = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    type = db.Column(db.String(80),nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.image,
            self.playlist,
            self.description,
            self.type
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.image = words[2].decode('utf-8')
            self.playlist = words[3].decode('utf-8')
            self.description = words[4].decode('utf-8')
            self.type = words[5].decode('utf-8')

##################################################################################################
# Podcast
##################################################################################################
class Podcast(db.Model):
    __tablename__ = 'podcast'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    image = db.Column(db.String(80),nullable=True)
    playlist = db.Column(db.String(80),nullable=True)
    country = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    style = db.Column(db.String(80),nullable=True)
    stars = db.Column(db.Integer,nullable=True)
    feed_url = db.Column(db.String(120),nullable=True)
    feed_filter = db.Column(db.String(80),nullable=True)
    pod_dir = db.Column(db.String(120),nullable=True)
    publisher = db.Column(db.String(80),nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    fav = db.Column(db.Boolean,nullable=True)
    retag = db.Column(db.Boolean,nullable=True)
    podcast_link_list = db.relationship('Podcast_Link', backref='podcast')
    episode_list = db.relationship('Episode', backref='podcast')

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.image,
            self.playlist,
            self.country,
            self.description,
            self.style,
            self.stars,
            self.feed_url,
            self.feed_filter,
            self.pod_dir,
            self.publisher,
            self.priority,
            self.fav,
            self.retag
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.image = words[2].decode('utf-8')
            self.playlist = words[3].decode('utf-8')
            self.country = words[4].decode('utf-8')
            self.description = words[5].decode('utf-8')
            self.style = words[6].decode('utf-8')
            self.stars = int(words[7])
            self.feed_url = words[8].decode('utf-8')
            self.feed_filter = words[9].decode('utf-8')
            self.pod_dir = words[10].decode('utf-8')
            self.publisher = words[11].decode('utf-8')
            self.priority = (words[12]=='True')
            self.fav = (words[13]=='True')
            self.retag = (words[14]=='True')

    def url_is_in_db(self, url):

        urls_in_db = [ str(ep.url) for ep in self.episode_list ]

        return (url in urls_in_db)

##################################################################################################
# Episode
##################################################################################################
class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80),nullable=True)
    url = db.Column(db.String(120),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    pub_date = db.Column(db.String(80),nullable=True)
    downloaded = db.Column(db.Boolean,nullable=True)
    local_file = db.Column(db.String(120),nullable=True)
    audio_size = db.Column(db.String(80),nullable=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'), nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}|{}|{}|{}|{}\n""".format(
            self.id,
            self.title,
            self.url,
            self.description,
            self.pub_date,
            self.downloaded,
            self.local_file,
            self.audio_size,
            self.podcast_id
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.title = words[1].decode('utf-8')
            self.url = words[2].decode('utf-8')
            self.description = words[3].decode('utf-8')
            self.pub_date = words[4].decode('utf-8')
            self.downloaded = (words[5].decode('utf-8') == 'True')           
            self.local_file = words[6].decode('utf-8')
            self.audio_size = words[7].decode('utf-8')
            self.podcast_id = int(words[8])
    
    def audio_size_txt(self):

        audio_size_txt = ''
        if self.audio_size:
            audio_size_txt = "{:d} MB".format(int(float(self.audio_size) / 1000 / 1000))
        return audio_size_txt

    def pub_date_txt(self):

        return self.pub_date[0:10]

    def pub_date_feed_txt(self):

        pub_date = datetime.datetime.strptime(self.pub_date, '%Y.%m.%d-%H:%M:%S')

        return pub_date.strftime("%a, %d %b %Y %H:%M:%S")

##################################################################################################
# Radio Link
##################################################################################################
class Radio_Link(db.Model):
    __tablename__ = 'radio_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    url = db.Column(db.String(120),nullable=True)
    radio_id = db.Column(db.Integer, db.ForeignKey('radios.id'), nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.url,
            self.radio_id
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.url = words[2].decode('utf-8')
            self.radio_id = int(words[3])

##################################################################################################
# Artist Link
##################################################################################################
class Artist_Link(db.Model):
    __tablename__ = 'artist_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    url = db.Column(db.String(120),nullable=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.url,
            self.artist_id
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.url = words[2].decode('utf-8')
            self.artist_id = int(words[3])

##################################################################################################
# Podcast Link
##################################################################################################
class Podcast_Link(db.Model):
    __tablename__ = 'podcast_link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    url = db.Column(db.String(120),nullable=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'), nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}\n""".format(
            self.id, 
            self.name, 
            self.url,
            self.podcast_id
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.url = words[2].decode('utf-8')
            self.podcast_id = int(words[3])

##################################################################################################
# Bookmark
##################################################################################################
class Bookmark(db.Model):
    __tablename__ = 'bookmark'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120),nullable=True)
    image_url = db.Column(db.String(120),nullable=True)
    priority = db.Column(db.Integer, nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}\n""".format(
            self.id, 
            self.url,
            self.image_url,
            self.priority
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.url = words[1].decode('utf-8')
            self.image_url = words[2].decode('utf-8')
            self.priority = int(words[3])

##################################################################################################
# Preset
##################################################################################################
class Preset(db.Model):
    __tablename__ = 'preset'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    description = db.Column(db.String(120),nullable=True)
    url = db.Column(db.String(120),nullable=True)
    radio_id = db.Column(db.Integer, db.ForeignKey('radios.id'), nullable=True)

    def export_string(self):

        data_string = u"""{}|{}|{}|{}|{}\n""".format(
            self.id, 
            self.name,
            self.description,
            self.url,
            self.radio_id
        ).encode('utf-8')

        return data_string

    def import_string(self, data_string):

        words = data_string.split("|")

        id = int(words[0])
        if (id == self.id):
            self.name = words[1].decode('utf-8')
            self.description = words[2].decode('utf-8')
            self.url = words[3].decode('utf-8')
            self.radio_id = int(words[4])

    def radio_name(self):
        radio = Radios.query.filter_by(id=self.radio_id).first()
        return radio.name
