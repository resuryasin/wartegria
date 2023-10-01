from flask_restful import Resource, reqparse
from app import db
from app.models import Warteg

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
