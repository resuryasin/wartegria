from flask import Flask
from flask_restful import Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warteg.db'

db = SQLAlchemy(app)

class Warteg(db.Model):
    id = db.Column('warteg_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(100), nullable=True)
    addr = db.Column(db.String(200), nullable=True) 
    dist = db.Column(db.Integer, nullable=True)
    def __init__(self, name, desc, addr, dist):
        self.name = name
        self.desc = desc
        self.addr = addr
        self.dist = dist

db.create_all()

class WartegRes(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id')
        self.parser.add_argument('name')
        self.parser.add_argument('desc')
        self.parser.add_argument('addr')
        self.parser.add_argument('dist')
    def get(self):
        listWarteg = {}
        for warteg in Warteg.query.all():
            listWarteg[str(warteg)] = {'id':warteg.id,'name':warteg.name,'desc':warteg.desc,'addr':warteg.addr,'dist':warteg.dist}
        import json
        return json.dumps(listWarteg)
    def post(self):
        data = self.parser.parse_args()
        warteg = Warteg(data['name'],data['desc'],data['addr'],data['dist'])
        db.session.add(warteg)
        db.session.commit()
        return data
    def delete(self):
        data = self.parser.parse_args()
        warteg = Warteg.query.filter_by(id=data['id']).first()
        db.session.delete(warteg)
        db.session.commit()
        return 'success'