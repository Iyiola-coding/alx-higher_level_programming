#!/usr/bin/python3
"""defining to_json_string function"""


import json


def to_json_string(my_obj):
    """"return json representation of an object"""
        return json.dumps(my_obj)
