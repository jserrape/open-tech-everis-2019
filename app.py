import os, sys

import sqlite3 as sql

import json

from flask import Flask, redirect
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort
from flask import Response
from flask import send_from_directory


#BBDD
'''
conn = sql.connect('database.db')
print("Opened database successfully")
conn.execute('DROP TABLE IF EXISTS usuario')
conn.execute('CREATE TABLE IF NOT EXISTS usuario (email TEXT PRIMARY KEY, password TEXT, nombre TEXT)')
print("Tables created successfully")
conn.close()
with sql.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO usuario (email, password, nombre) VALUES (?,?,?)",('ejemplo@gmail.com', 'password', 'Juan Carlos') )
    con.commit()

con.close()
'''


# Información general
server_info = {}
server_info['desarrolladores'] = {'1','2','3'}
server_info['email'] = 'juan.carlos.wow.95@gmail.com'
server_info['twitter'] = '@xenahort'
server_info['server_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-servidor'
server_info['app_repository']  = 'https://github.com/xenahort/-TFM-Generador-de-historias-Android'


# Flask initialisation
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    respons = {}
    respons['status'] = 404
    respons = jsonify(respons)
    respons.status_code = 404
    return respons

@app.route('/')
def index():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/'
    respons = jsonify(respons)
    respons.status_code = 201
    return respons
    
@app.route('/list/users')
def list_users():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/list/users'

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM usuario')
        data_max = []
        for row in cur.fetchall():
            data_min = {}
            data_min['email'] = row[0]
            data_min['password'] = row[1]
            data_min['nombre'] = row[2]
            data_max.append(data_min)
    con.close()
    
    respons['users'] = json.dumps(data_max)
    
    respons = jsonify(respons)
    respons.status_code = 201
    
    return respons


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)