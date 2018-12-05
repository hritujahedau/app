import logging
from cerberus import Validator
import logger


def validate_data(schema_type, data):
    v = Validator(schema_type)
    if v.validate(data):     
        data = v.normalized(data)
        return data
    else:
        print "Not Validated"
