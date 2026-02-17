# ===========================
# Test: GET missing counter returns 404
# Author: Kaleab Gebru
# Date: 2026-02-14
# Description: Ensure GET returns JSON 404 when counter does not exist.
# ===========================

from flask import Flask, jsonify
from . import status

app = Flask(__name__)

COUNTERS = {}

def counter_exists(name):
    """Check if counter exists"""
    return name in COUNTERS

@app.route("/counters/<name>", methods=["GET"])
def get_counter(name):
    """Retrieve an existing counter"""
    if not counter_exists(name):
        return jsonify({"error": f"Counter {name} not found"}), status.HTTP_404_NOT_FOUND
    return jsonify({name: COUNTERS[name]}), status.HTTP_200_OK
