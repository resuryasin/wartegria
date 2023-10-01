from flask_restful import Resource, reqparse
from app import db
from app.models import WartegModel

class WartegResorce(Resource):
    def __init__(self):
        self.model = WartegModel
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id')
        self.parser.add_argument('name')
        self.parser.add_argument('desc')
        self.parser.add_argument('addr')
        self.parser.add_argument('dist')
    def get(self):
        listWarteg = {}
        for warteg in self.model.query.all():
            listWarteg[str(warteg)] = {'id':warteg.id,'name':warteg.name,'desc':warteg.desc,'addr':warteg.addr,'dist':warteg.dist}
        import json
        return json.dumps(listWarteg)
    def post(self):
        data = self.parser.parse_args()
        warteg = self.model(data['name'],data['desc'],data['addr'],data['dist'])
        db.session.add(warteg)
        db.session.commit()
        return data
    def delete(self):
        data = self.parser.parse_args()
        warteg = self.model.query.filter_by(id=data['id']).first()
        db.session.delete(warteg)
        db.session.commit()
        return 'success'
