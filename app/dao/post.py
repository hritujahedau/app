from flask import Flask, request
from flask_restful import Resource, Api
from flask import session
from datetime import datetime

import django
django.setup()
from Agro.models import Post, User, DataInfo


def dao_create_post(data, user_id):
    try:
        app_user = User.objects.get(id=user_id)
        print "create post"
        new_post = Post.objects.create(
                        user=app_user,
                        time=datetime.now(),
                        is_deleted=False
                        )
        print "post created"
        json_tree = data["data"]
        for json_object in json_tree:
            if json_object["data_type"] == "DataInfo":
                for json_data in json_object["data"]:
                    new_data = DataInfo.objects.create(
                                    data_info_type=json_data['data_info_type'],
                                    value=json_data['value'],
                                    post=new_post
                                    )
                    new_data.save()
        return True
    except User.DoesNotExist:
        return False


def dao_update_post(data, post):
    try:
        json_tree = data["data"]
        for json_object in json_tree:
            if json_object["data_type"] == "DataInfo":
                for json_data in json_object["data"]:
                    new_data = DataInfo.objects.create(
                                    data_info_type=json_data['data_info_type'],
                                    value=json_data['value'],
                                    post=post
                                    )
                    new_data.save()
        return True


    except:
        return False


def dao_delete_data_info(post):
    try:

        data_info_objects = DataInfo.objects.filter(post=post)
        for dataInfoObject in data_info_objects:
            dataInfoObject.is_deleted = True
            dataInfoObject.deleted_time = datetime.now()
            dataInfoObject.save()
        return True
    except:
        return False



