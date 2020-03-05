from flask import Flask, jsonify, request
import requests, json
import datetime
app = Flask(__name__)

@app.route("/temperature", methods=['GET'])
def get_temperature():
    api_key = "2c6f9155611ff8fb1e08db06446cc8bc"
    city = "Portland"
    state = "Oregon"
    query_date = str(datetime.datetime.now())

    current_temp = get_temperature_from_web(city,state,api_key)
    response_json = '{"query_time": "'+query_date+'", "temperature": "'+ current_temp +'"}'
    return response_json

def get_temperature_from_web(city,state,api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&appid="+api_key+"&units=imperial"
    r = requests.get(url)
    r_temp = r.json()["main"]["temp"]
    return str(r_temp)

