from flask_restful import Resource, Api

class Ping(Resource):
    def get(self):
        return {'Message':'Ok'}