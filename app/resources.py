from flask import jsonify, request
from flask_restful import Resource, reqparse
from app.models import WartegModel
from app import db 

class WartegResource(Resource):
    def __init__(self):
        self.model = WartegModel
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('name')
        self.parser.add_argument('desc')
        self.parser.add_argument('addr')
        self.parser.add_argument('dist')

    def get(self):
        def _get_warteg_data(warteg):
            return {
                'id': warteg.id,
                'name': warteg.name,
                'desc': warteg.desc,
                'addr': warteg.addr,
                'dist': warteg.dist
            }

        args = self.parser.parse_args()
        if args.get('id'):
            warteg = self.model.query.filter_by(id=args['id']).first()
            if warteg:
                warteg_data = _get_warteg_data(warteg)
                return jsonify(warteg_data)
            else:
                return jsonify({'message': 'Warteg not found'})
        else:
            wartegs = self.model.query.all()
            warteg_list = []
            for warteg in wartegs:
                warteg_data = _get_warteg_data(warteg)
                warteg_list.append(warteg_data)
            return jsonify(warteg_list)

    def post(self):
        data = request.get_json()  # Parse JSON data from the request
        if not data:
            return jsonify({'message': 'Invalid JSON data'})

        warteg = self.model(name=data.get('name'), desc=data.get('desc'), addr=data.get('addr'), dist=data.get('dist'))
        db.session.add(warteg)
        db.session.commit()
        return jsonify({'message': 'Warteg created successfully', 'data': data})

    def delete(self):
        data = self.parser.parse_args()
        warteg = self.model.query.filter_by(id=data['id']).first()
        if warteg:
            db.session.delete(warteg)
            db.session.commit()
            return jsonify({'message': 'Warteg deleted successfully'})
        else:
            return jsonify({'message': 'Warteg not found'})
