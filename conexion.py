import pymysql
from flask import g

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='SIGEPI_DB',
            cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)

def test_connection():
    db = get_db()
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            result = cursor.fetchone()
            return f"Database connected. Version: {result['VERSION()']}"
    except Exception as e:
        return f"Database not connected. Error: {e}"
    
