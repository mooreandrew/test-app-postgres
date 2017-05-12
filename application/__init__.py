from flask import Flask, request
import os
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))

db = SQLAlchemy(app)
