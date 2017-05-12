from application import app, db
import os
from flask import Flask, render_template, request
import traceback
import sys
from sqlalchemy.sql import text

@app.route('/', methods=['POST', 'GET'])
def index():

    status = 'N/A'
    sql = ''
    if 'sql' in request.form:
        sql = request.form['sql']
        try:
            sql = request.form['sql']
            db.session.execute(text(sql))
            status = 'Success'
        except:

            status = traceback.format_exc()

    return render_template('index.html', status=status, sql=sql)


@app.route('/health')
def health():
    return('ok')
