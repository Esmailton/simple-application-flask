from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
db =SQLAlchemy(app)
ma = Marshmallow(app)
CORS = CORS(app)