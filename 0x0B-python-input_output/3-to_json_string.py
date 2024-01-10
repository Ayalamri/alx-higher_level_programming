#!/usr/bin/python3
"""
Function to convert an object to its JSON representation
"""

import json

def to_json_string(my_obj):
    """
    Convert the given object to its JSON representation.
    """
    return json.dumps(my_obj)
