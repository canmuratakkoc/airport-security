from flask import Flask
from flask_cors import CORS
from .socket_events import socketio


def create_app(test = False):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')
    app.config['TESTING'] = test

    socketio.init_app(app, cors_allowed_origins="*")

    from app.routes import analyze_blueprint
    from app.routes.main import main_blueprint

    app.register_blueprint(analyze_blueprint, url_prefix='/analyze')
    app.register_blueprint(main_blueprint)

    return app
