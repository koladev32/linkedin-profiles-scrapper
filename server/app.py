from flask import Flask
from flask import Flask, jsonify, request

from .client import ProxyCurlClient

app = Flask(__name__)

client = ProxyCurlClient()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/profiles/", methods=["POST"])
def retrieve_profiles():
    if "search" not in request.json:
        return jsonify({"erorr": "Missing search parameter"}), 400
    
    data = client.get_profiles(request.json["search"])
    
    return jsonify(data), 200