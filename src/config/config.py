import os
from .constants import DEV_MODE, PRD_MODE, QA_MODE, STG_MODE

class LOCAL:
    #[Credentials]
    GOOGLE_APPLICATION_CREDENTIALS = 'db_keys/nrg_dev.json'
    CREDENTIALS_FIREBASE_SDK_PATH = 'db_keys/nrg_dev.json'
 
    #[Firebase]
    KATCH_FIREBASE_DB_URL='https://katch-nrg-nonprod.firebaseio.com/'
    CURRENT_ENV = DEV_MODE
class DEV:
    #[Credentials]
    GOOGLE_APPLICATION_CREDENTIALS = 'db_keys/nrg_dev.json'
    CREDENTIALS_FIREBASE_SDK_PATH = 'db_keys/nrg_dev.json'
 
    #[Firebase]
    KATCH_FIREBASE_DB_URL='https://katch-nrg-nonprod.firebaseio.com/'
    CURRENT_ENV = DEV_MODE
class QA:
    #[Credentials]
    GOOGLE_APPLICATION_CREDENTIALS = 'db_keys/nrg_dev.json'
    CREDENTIALS_FIREBASE_SDK_PATH = 'db_keys/nrg_dev.json'
 
    #[Firebase]
    KATCH_FIREBASE_DB_URL='https://katch-nrg-nonprod.firebaseio.com/'
    CURRENT_ENV = QA_MODE
class STG:
    #[Credentials]
    GOOGLE_APPLICATION_CREDENTIALS = 'db_keys/nrg_staging.json'
    CREDENTIALS_FIREBASE_SDK_PATH = 'db_keys/nrg_staging.json'
 
    #[Firebase]
    KATCH_FIREBASE_DB_URL='https://katch-nrg-staging-106c2.firebaseio.com/'
    CURRENT_ENV = STG_MODE
class PRD:
    #[Credentials]
    GOOGLE_APPLICATION_CREDENTIALS = 'db_keys/nrg_prod.json'
    CREDENTIALS_FIREBASE_SDK_PATH = 'db_keys/nrg_prod.json'
 
    #[Firebase]
    KATCH_FIREBASE_DB_URL='https://katch-nrg-6b8c7-default-rtdb.firebaseio.com/'
    CURRENT_ENV = PRD_MODE
class Configuration:
    Env = LOCAL
    
    #[Credentials]
    GOOGLE_APPLICATION_CREDENTIALS = Env.GOOGLE_APPLICATION_CREDENTIALS
    CREDENTIALS_FIREBASE_SDK_PATH = Env.CREDENTIALS_FIREBASE_SDK_PATH
    APP_SECRET_KEY = 'secret-key'
    # FIREBASE_WEB_API_KEY = Env.FIREBASE_WEB_API_KEY
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS

    #[Firebase]
    KATCH_FIREBASE_DB_URL = Env.KATCH_FIREBASE_DB_URL

    print('ENV {0}'.format(Env))
    print('Current Mode {0}'.format(Env))
