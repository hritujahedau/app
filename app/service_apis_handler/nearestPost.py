from views.view import post_as_json
import django
django.setup()


from Agro.models import Post, Location
from redis import Redis
client = Redis()



def get_nearestPost(**params):
    location = params.get('location')
    city = location.get('city', "")
    state = location.get('state', "")
    topic_name = "{}-{}",format(city,state)
    if client.get(topic_name):
        topic, posts = client.brpop(topic_name, timeout=0)
    else:
        user_location = Location.objects.get(state=location['state'],
                                         district=location['district'],
                                         country=location['country'])
        posts = [post_as_json(post)\
        for post in Post.objects.filter\
        (is_deleted=False, location=user_location)\
        ]
        client.lpush(topic_name, posts)

    return posts




