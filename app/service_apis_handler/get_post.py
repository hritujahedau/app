from views.view import post_as_json
import django
from redis import Redis

django.setup()
from Agro.models import Post, User

redis_client = Redis()


def get_post(post_id=None, user_id=None):
    try:
        if post_id and user_id:
            user = User.objects.get(id=user_id, is_deleted=False)
            return [post_as_json(post) for post in Post.objects.filter(is_deleted=False, user=user, id=post_id)]
        if post_id:
            post = Post.objects.get(is_deleted=False, id=post_id)
            return post_as_json(post)
        if user_id:
            user = User.objects.get(id=user_id, is_deleted=False)
            return [post_as_json(post) for post in Post.objects.filter(is_deleted=False, user=user)]

            # posts = Post.objects.get(is_deleted=False, id=post_id)
            # redis_client.lpush(topic_name, event_data)
            # topic, data = client.brpop(topics_consumed, timeout=0)
            return []
        print "get all post"
        return [post_as_json(post) for post in Post.objects.filter(is_deleted=False)]

    except Post.DoesNotExist:
        return {'message': 'post not exists'}
    except User.DoesNotExist:
        return {'message': 'user not exists'}

