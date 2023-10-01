from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warteg.db'
db = SQLAlchemy(app)
