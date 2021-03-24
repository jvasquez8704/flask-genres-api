from flask_restful import Api
from dotenv import load_dotenv

from config.setup import Startup
from services.genres import Genre

load_dotenv()

app = Startup.app
api = Api(app)

@app.before_first_request
def loading_config():
    print('GENRES API STARTED!')


api.add_resource(Genre, '/genres')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context='adhoc')
     
