from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warteg.db'
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

from app.resources import WartegResorce
api.add_resource(WartegResorce, '/api/warteg/')

from app.views import home