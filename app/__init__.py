from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from .config import Config

app = Flask(__name__)

CONFIG = Config()

app.config["SQLALCHEMY_DATABASE_URI"] = CONFIG.SQLITE_DATABASE
app.config['SECRET_KEY'] = "CocoCoco"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import Radios, Artist, Playlist, Podcast, Artist_Link, Radio_Link, Podcast_Link

from .dbman import DBManager
db_manager = DBManager(db)

from download_manager import DownloadManager
download_manager = DownloadManager()

from radio import RadioPlayer
radio_player = RadioPlayer()

from .views_base import base
from .views_player import player
from .views_radio import radio
from .views_artist import artist
from .views_playlist import playlist
from .views_podcast import podcast
from .views_cxn import cxn
from .views_mobile import mobile

app.register_blueprint(base)
app.register_blueprint(player)
app.register_blueprint(radio)
app.register_blueprint(artist)
app.register_blueprint(playlist)
app.register_blueprint(podcast)
app.register_blueprint(cxn)
app.register_blueprint(mobile)
