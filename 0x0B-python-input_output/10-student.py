#!/usr/bin/python3
"""
Defines a Student class with public instance attributes and a to_json method.
"""

class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        result = {}
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            for attribute in attrs:
                if hasattr(self, attribute):
                    result[attribute] = getattr(self, attribute)
        else:
            attributes = dir(self)
            for attribute in attributes:
                if not attribute.startswith('_'):
                    value = getattr(self, attribute)
                    if isinstance(value, (list, dict, str, int, bool)):
                        result[attribute] = value

        return result
