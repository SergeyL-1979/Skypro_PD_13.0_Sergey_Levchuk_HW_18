#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restx import Api

from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from config import Config
from setup_db import db


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app=app, title="SkyPro: HW_architecture_lesson_18", )
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run(port=10000)
