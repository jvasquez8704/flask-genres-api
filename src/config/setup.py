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
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
