#!/usr/bin/python3
"""v1 starting point"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns v1 status"""
    return jsonify({"status": "OK"})
