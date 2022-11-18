from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from WebServer.MockServer.MockApp import api_bp
    app.register_blueprint(api_bp, url_prefix='/mockServer')

    return app


if __name__ == "__main__":
    app = create_app("MockConfig")
    app.run(debug=True)