#!/usr/bin/env python
from flask import jsonify
from flask import Flask, render_template, request
import json
import time
import datetime
from database_utils import getConn
import os
import base64
import logging
from time import gmtime
import base64


host = os.environ.get('MYSQL_HOST'),
user = os.environ.get('MYSQL_USER'),
password = os.environ.get('MYSQL_ROOT_PASSWORD'),
db = os.environ.get('MYSQL_DATABASE')

app = Flask(__name__)


@app.route('/')
def display_menu():
    return render_template('menu.html')


@app.route('/filter/region', methods=['GET', 'POST'])
def filter_by_region():
    if request.method == 'POST':

        # Validate myid
        try:
            myid = int(request.form['myid'])
            if 1 <= myid <= 4:
                print("Valid request..")
            else:
                print("ID must be between 1 and 4")

        except ValueError:
            print("Rating must be a valid integer..")

        cnx = getConn(host, user, password, db)
        cur = cnx.cursor()
        query = """select region_name from region where id=%s;"""
        cur.execute(query, (myid,))
        rows = cur.fetchall()
        dict_data = []
        for a in rows:
            dict_data.append({'region_name': a})

        return jsonify(dict_data)
    return render_template('filter_region.html')


app.run(host="0.0.0.0")
