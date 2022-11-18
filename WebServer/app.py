from flask import Flask, Blueprint
from flask_restful import Api
from WebServer.Resource.Hello import Hello
api_bp = Blueprint('mockServer', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/hello')