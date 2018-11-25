# services/users/project/__init__.py

import os  # new
from flask import Flask, jsonify


# instantiate the app, esta instaciando este mismo archivo 
app = Flask(__name__)

# set config
#app.config.from_object('project.config.DevelopmentConfig')  # new
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new

import sys
#print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])

def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })