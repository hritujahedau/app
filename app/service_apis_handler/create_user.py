from validators.data_validator import validate_data
from validators.validator_schemas import user_schema
from views.view import user_as_json

import django
django.setup()

from Agro.models import User, Location


def get_user_details(user_id):
        try:
            if user_id:
                user = User.objects.get(id=user_id)
                return user_as_json(user)
            return [
                user_as_json(user)
                for user in User.objects.all()
            ]
        except User.DoesNotExist:
            return {'message': 'user does not exist'}
        except User.MultipleObjectsReturned:
            return {'message': 'Multiple users exist'}


def create_user(**data):

        data = validate_data(user_schema, data)
        location = data['location']
        try:
            user = User.objects.get(mobile_number=data['mobile_number'])
        except User.DoesNotExist:
            try:
                user_location = Location.objects.get(state=location['state'],
                                                     district=location['district'],
                                                     country=location['country'])
                User.objects.create(first_name=data['first_name'],
                                    last_name=data['last_name'],
                                    profile_pic_url=data['profilePic'],
                                    location=user_location,
                                    mobile_number=data['mobile_number'])
                return True

            except Location.DoesNotExist:
                try:

                    user_location = Location.objects.create(
                        district=location['district'],
                        state=location['state'],
                        country=location['country'])
                    User.objects.create(first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        profile_pic_url=data['profilePic'],
                                        location=user_location,
                                        mobile_number=data['mobile_number'])

                    return True
                except Exception as err:
                    print err
                    return False

        except:
            return False
