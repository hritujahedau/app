from flask import request, app
from flask_restful import Resource
from service_apis_handler.create_user import get_user_details, create_user

from exception.error_handler import ErrorHandler


class Users(Resource):
    @ErrorHandler(app)
    def get(self, user_id=None):
        user = get_user_details(user_id)
        return user

    @ErrorHandler(app)
    def post(self):
        request_data = request.json
        user = create_user(**request_data)
        if user:
            return {'message': 'User Created'}
        return {'message': 'User Not Created'}
