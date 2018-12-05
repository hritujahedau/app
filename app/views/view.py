import django
django.setup()
from Agro.models import  Location, DataInfo


def user_as_json(user):
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "location": [location_as_json(data) for data in Location.objects.filter(id=user.location.id)],
        "profile_pic_url": user.profile_pic_url,
        "mobile_number": user.mobile_number
    }


def location_as_json(location):
    return {
        "state": location.state,
        "country": location.country,
        "district": location.district
    }


def post_data_as_json(data):
    return {
        "id": data.id,
        "data_info_type": data.data_info_type,
        "value": data.value,
        "is_deleted": data.is_deleted,
        "deleted_time": str(data.deleted_time)
    }        


def post_as_json(user_post):
    return {
        "id": user_post.id,
        "time": str(user_post.time),
        "user": user_post.user.id,
        "is_deleted": user_post.is_deleted,
        "data": [post_data_as_json(data) for data in DataInfo.objects.filter(is_deleted=False, post=user_post.id)]
    }
