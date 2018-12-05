from validators.validator_schemas import post_schema
from validators.data_validator import validate_data

import django
django.setup()
from Agro.models import Post, User


from dao.post import dao_create_post, dao_delete_data_info, dao_update_post


def create_post(user_id, data):
    try:
        user = User.objects.get(id=user_id)
        data = validate_data(post_schema, data)
        is_user_created = dao_create_post(data, user_id)
        if is_user_created:
            return {'message': 'Post created'}
        return {'message': 'user not created'}

    except User.DoesNotExist:
        return {'message': 'User Not exists'}


def update_post(post_id, request_data, user_id):
        try:
            post = Post.objects.get(id=post_id, is_deleted=False)
            user = User.objects.get(id=user_id)
            if post.user == user:
                if validate_data(post_schema, request_data):
                    is_data_info_deleted = dao_delete_data_info(post)
                    if is_data_info_deleted:
                        is_post_updated = dao_update_post(request_data, post)
                        if is_post_updated:
                            return {'message': 'updated'}
                    return {'message': 'not updated'}
            return {'message': 'invalid user'}
        except Post.DoesNotExist:
            return {'message': 'post not exist'}
        except User.DoesNotExist:
            return {'message': 'User not exist'}


def delete_post(post_id, user_id):
    try:
        user_post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
        if user_post.user == user:
            is_post_deleted = dao_delete_data_info(user_post)
            if is_post_deleted:
                user_post.is_deleted = True
                user_post.save()
                return {'message': 'post deleted'}
            return {'message': 'Post not deleted'}

    except Post.DoesNotExist:
        return {'message': 'post not exist'}
    except User.DoesNotExist:
        return {'message': 'post not exist'}
