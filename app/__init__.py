from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
from app.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

app = Flask(__name__) 
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
api = Api(app)
CORS(app)

from app.resources import WartegResorce
api.add_resource(WartegResorce, '/api/warteg/')

from app.views import home
