from flask import Flask
from flask_restful import Api

from api_model import *

api = Api(app)

api.add_resource(WartegRes,'/api/warteg/')

if __name__ == '__main__':
    app.run(host="localhost", port=5001)