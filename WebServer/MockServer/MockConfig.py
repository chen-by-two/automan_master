from flask import Blueprint
from flask_restful import Api
from WebServer.MockServer.MockApi.Demo import Hello
from WebServer.MockServer.MockApi.Demo2 import Good


api_bp = Blueprint('mockServer', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Hello, '/Hello')

