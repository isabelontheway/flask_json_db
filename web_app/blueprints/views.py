import sqlite3
from flask import Blueprint, current_app, g, render_template

bp = Blueprint('web_app', __name__)


def connect_db():
    conn = sqlite3.connect(current_app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@bp.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select * from students order by id desc')
    student_entries = cur.fetchall()
    return render_template('show_entries.html', entries=student_entries)
