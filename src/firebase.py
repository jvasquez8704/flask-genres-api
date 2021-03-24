import firebase_admin
from firebase_admin import credentials, db

import json
import requests
import uuid
from config.config import Configuration 
from config.constants import GENRES_SCHEME

cred = credentials.Certificate(Configuration.GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    'databaseURL': Configuration.KATCH_FIREBASE_DB_URL
})

def get_genres():
    return db.reference(GENRES_SCHEME).get()