from flask import Flask, Blueprint
from flask_restful import Api
from WebServer.MockServer.MockApi.Demo import Hello
from WebServer.MockServer.MockApi.Demo2 import Good

api_bp = Blueprint('mockServer', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(Good, '/Good')