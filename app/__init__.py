import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db_user = os.getenv("MYSQL_USER", "appuser")
    db_password = os.getenv("MYSQL_PASSWORD", "change_me")
    db_host = os.getenv("MYSQL_HOST", "db")
    db_name = os.getenv("MYSQL_DATABASE", "flaskdb")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from app.controllers.home_controller import home
    app.register_blueprint(home)

    with app.app_context():
        from app.models.note import Note
        db.create_all()

    return app
