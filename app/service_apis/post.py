from flask import request, app
from flask_restful import Resource
from exception.error_handler import ErrorHandler
from service_apis_handler.get_post import get_post
from service_apis_handler.create_post import create_post, update_post, delete_post



class PostHandler(Resource):
    @ErrorHandler(app)
    def get(self, post_id=None):
        params = request.headers
        user_id = params.get('user')
        post = get_post(post_id, user_id)
        return post

    @ErrorHandler(app)
    def post(self):
        request_data = request.json
        params = request.headers
        user_id = params.get('user')
        if not user_id:
            return {'message': 'no user id'}
        post = create_post(user_id, request_data)
        return post

    @ErrorHandler(app)
    def patch(self, post_id):
        request_data = request.json
        params = request.headers
        user_id = params.get('user')
        if post_id and user_id:
            return update_post(post_id, request_data, user_id)
        return {'message': 'No user id or post id'}

    @ErrorHandler(app)
    def delete(self, post_id):
        print "Delete"
        params = request.headers
        user_id = params.get('user')
        if user_id:
            return delete_post(post_id, user_id)
        return {'message': 'no user id'}

