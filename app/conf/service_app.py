from flask import Flask
from flask_restful import Api
from service_apis.ping import Ping
from service_apis.users import Users
from service_apis.post import PostHandler
from service_apis.postAction import PostActionHandler
from service_apis.nearestPost import NearestPost
from flask_cors import CORS

app = Flask('APP')
CORS(app)
api = Api(app)


api.add_resource(Ping, '/')
api.add_resource(Users, '/User/', '/User/<string:user_id>')
api.add_resource(PostHandler, '/post/', '/post/<string:post_id>')
api.add_resource(PostActionHandler, '/post/likes/', '/post/likes/<string:post_id>')
api.add_resource(NearestPost, '/post/nearestPost')

if __name__ == '__main__':
    app.run(host='localhost', port=2004, debug=True)



