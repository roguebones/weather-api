from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/temperature", methods=['GET'])
def get_temperature():
  return "Hello, World!"
