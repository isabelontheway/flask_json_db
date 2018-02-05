import os
from flask import Flask
from web_app.blueprints.views import bp, init_db, close_db


def create_app(config=None):
    app = Flask('web_app')

    config = app.config
    config.update(dict(
        DATABASE=os.path.join(app.root_path, 'students.db'),
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',

    ))
    config.update(config or {})
    config.from_envvar('FLASKR_SETTINGS', silent=True)

    app.register_blueprint(bp)
    register_cli(app)
    register_teardowns(app)

    return app


def register_cli(app):
    @app.cli.command('initdb')
    def init_db_command():
        init_db()
        print ('Initialized the database.')


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db_when_shutdown(error):
        close_db()
        print('Closed the database')
