from flask import Flask
from flask_cors import CORS

import logging
from datetime import timedelta
from config.config import Configuration 

class Startup:
    # Api config
    app = Flask(__name__)
    CORS(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = Configuration.APP_SECRET_KEY
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

    # Session config for future implementation (not work right now)
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)