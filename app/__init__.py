from flask import Flask
from flask_cors import CORS
from .socket_events import socketio
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()


def create_app(test = False):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')
    app.config['TESTING'] = test

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app, cors_allowed_origins="*")

    from app.routes import analyze_blueprint
    from app.routes.main import main_blueprint

    app.register_blueprint(analyze_blueprint, url_prefix='/analyze')
    app.register_blueprint(main_blueprint)

    return app
