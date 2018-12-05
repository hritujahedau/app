from flask_restful import Resource
from exception.error_handler import ErrorHandler
from flask import request, app
from service_apis_handler.nearestPost import get_nearestPost


class NearestPost(Resource):
    @ErrorHandler(app)
    def get(self):
        params = request.headers
        post = get_nearestPost(**params)
        return post

