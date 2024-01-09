#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or inherited from it, else False.
    """
    return isinstance(obj, a_class)
