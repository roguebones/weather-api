from flask import Flask, jsonify, request
import requests, json
import datetime
import sqlite3

app = Flask(__name__)

@app.before_first_request
def _run_on_start():
    sqliteConnection = sqlite3.connect('temperature_api_sqlite.db')
    create_table = '''CREATE TABLE IF NOT EXISTS temperature_responses (
                                id INTEGER PRIMARY KEY,
                                city TEXT NOT NULL,
                                state text NOT NULL,
                                query_time datetime,
                                temperature_f REAL NOT NULL);'''
    cursor = sqliteConnection.cursor()
    cursor.execute(create_table)
    sqliteConnection.commit()

@app.route("/temperature", methods=['GET'])
def get_temperature():

    # Set up data
    api_key = "2c6f9155611ff8fb1e08db06446cc8bc"
    city = "Portland"
    state = "Oregon"
    query_time = str(datetime.datetime.now())
    current_temp = get_temperature_from_web(city,state,api_key)

    # Insert in to table
    sqliteConnection = sqlite3.connect('temperature_api_sqlite.db')
    value_list = [city,state,query_time,current_temp]
    insert_temperature(sqliteConnection,value_list)

    # Rrovide response
    response_dict = {"query_time": query_time, "temperature": current_temp}
    return response_dict

def get_temperature_from_web(city,state,api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&appid="+api_key+"&units=imperial"
    r = requests.get(url)
    r_temp = r.json()["main"]["temp"]
    return str(r_temp)
 
 
def insert_temperature(conn, temperature_list):

    sql = ''' INSERT INTO temperature_responses(city,state,query_time,temperature_f)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, temperature_list)
    return cur.lastrowid

