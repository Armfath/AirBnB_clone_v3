#!/usr/bin/python3
"""API app for AirBnB project"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def close_database_connection(exception=None):
    """Close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST') or '0.0.0.0',
            port=int(getenv('HBNB_API_PORT') or 5000),
            threaded=True)
