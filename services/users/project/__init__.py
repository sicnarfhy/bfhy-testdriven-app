# services/users/project/__init__.py

import os  # new
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy  # new


# instantiate the app, esta instaciando este mismo archivo 
app = Flask(__name__)

# set config
#app.config.from_object('project.config.DevelopmentConfig')  # new
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new

# instantiate the db
db = SQLAlchemy(app)  # new

# model
class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

#import sys
#print(app.config, file=sys.stderr)

# routes
@app.route('/users/ping', methods=['GET'])

def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })