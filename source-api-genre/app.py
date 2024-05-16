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


@app.route('/filter/genre', methods=['GET', 'POST'])
def filter_genre():
    if request.method == 'POST':
        # Validate myid
        try:
            myid = int(request.form['myid'])
            if 1 <= myid <= 12:
                print("Valid request..")
            else:
                print("ID must be between 1 and 12")

        except ValueError:
            print("ID must be a valid integer..")

        cnx = getConn(host, user, password, db)
        cur = cnx.cursor()
        query = """select genre_name from genre where id=%s;"""
        cur.execute(query, (myid,))
        rows = cur.fetchall()
        dict_data = []
        for a in rows:
            dict_data.append({'genre': a})

        return jsonify(dict_data)
    return render_template('filter_genre.html')


app.run(host="0.0.0.0")
