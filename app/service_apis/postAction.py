from flask_restful import Resource
from flask import request, app

from exception.error_handler import ErrorHandler


class PostActionHandler(Resource):
    @ErrorHandler(app)
    def get(self):
        return {'message': 'Not implemented yet'}

    @ErrorHandler(app)
    def post(self, post_id):
        return {'message': 'Not implemented yet'}

