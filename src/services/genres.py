from flask_restful import Resource, reqparse
from firebase import get_genres

class Genre(Resource):
    def get(self):
        genres = get_genres()
        if genres:
            return {"data": genres}, 200
        return {'status_code': 404, 'custom_code': 'GENRES_NOT_FOUND', 'message': 'Genres not found'}, 404
