from flask import Flask, jsonify, request
import requests, json
app = Flask(__name__)

@app.route("/temperature", methods=['GET'])
def get_temperature():
    api_key = "2c6f9155611ff8fb1e08db06446cc8bc"
    city = "Portland"
    state = "Oregon"
    return get_temperature_from_web(city,state,api_key)

def get_temperature_from_web(city,state,api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&appid="+api_key+"&units=imperial"
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&appid="+api_key)
    r_temp = r.json()["main"]["temp"]
    return str(r_temp)
