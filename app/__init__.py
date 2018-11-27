from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from .globals import GlobalValues

app = Flask(__name__)

app.secret_key = "CocoCoco"

global_values = GlobalValues()

app.config["SQLALCHEMY_DATABASE_URI"] = global_values.database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from .dbman import DBManager
db_manager = DBManager(db)

from radio import RadioPlayer

radio_player = RadioPlayer()

from .views_player import player
from .views_radio import radio
from .views_artist import artist
from .views_playlist import playlist
from .views_podcast import podcast

app.register_blueprint(player)
app.register_blueprint(radio)
app.register_blueprint(artist)
app.register_blueprint(playlist)
app.register_blueprint(podcast)
