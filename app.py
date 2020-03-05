from flask import Flask, jsonify, request
import requests, json
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.before_first_request
def _run_on_start():

    # Runs before first request and creates the temperature_responses table if it doesn't exist
    conn = sqlite3.connect('temperature_api_sqlite.db')
    create_table = '''CREATE TABLE IF NOT EXISTS temperature_responses (
                                id INTEGER PRIMARY KEY,
                                city TEXT NOT NULL,
                                state text NOT NULL,
                                query_time datetime,
                                temperature_f REAL NOT NULL);'''
    cursor = conn.cursor()
    cursor.execute(create_table)
    conn.commit()

@app.route("/temperature", methods=['GET'])
def get_temperature():

    # Set up data
    api_key = "2c6f9155611ff8fb1e08db06446cc8bc"
    conn = sqlite3.connect('temperature_api_sqlite.db')

    city = "Portland"
    state = "Oregon"
    query_time = datetime.now()

    # Check if there is a recent response before searching web
    most_recent_temp_row = get_most_recent_temp(conn,city,state)
    most_recent_temp_time = most_recent_temp_row[3]
    most_recent_temp_f = most_recent_temp_row[4]
    time_diff = (query_time - datetime.strptime(most_recent_temp_time, "%Y-%m-%d %H:%M:%S.%f")).seconds / 60

    # Check if most recent record is within 5 minutes from response
    if time_diff <= 5.0:
        current_temp = most_recent_temp_f
    else:
        current_temp = get_temperature_from_web(city,state,api_key)

        # Insert in to table
        temperature_list = [city,state,str(query_time),current_temp]
        insert_temperature(conn,temperature_list)

    # Provide response
    response_dict = {"query_time": str(query_time), "temperature": current_temp}
    return response_dict

def get_temperature_from_web(city,state,api_key):

    # Uses openweathermap API to get temp data for a city and state
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+state+"&appid="+api_key+"&units=imperial"
    r = requests.get(url)
    r_temp = r.json()["main"]["temp"]
    return str(r_temp)
 
def insert_temperature(conn, temperature_list):

    # Inserts in to the temperature_responses table
    sql = ''' INSERT INTO temperature_responses(city,state,query_time,temperature_f) VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, temperature_list)
    conn.commit()
    return cur.lastrowid

def get_most_recent_temp(conn,req_city,req_state):

    # Gets the most recent 1 record for a given city and state in order to do date differences
    sql = ''' SELECT * FROM temperature_responses WHERE city =? AND state =? ORDER BY id DESC LIMIT 1 '''
    cur = conn.cursor()
    cur.execute(sql, (req_city,req_state,))
    row = list(cur.fetchone())
    return row

