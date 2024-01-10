#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure
(list, dictionary, string, integer, and boolean) for JSON serialization
of an object.
"""

def class_to_json(obj):
    """Converts an instance of a class to a JSON-serializable dictionary."""
    result = {}
    
    # Get all attributes of the object
    attributes = dir(obj)
    
    for attribute in attributes:
        # Exclude private attributes and methods
        if not attribute.startswith('_'):
            value = getattr(obj, attribute)
            
            # Only include serializable data types
            if isinstance(value, (list, dict, str, int, bool)):
                result[attribute] = value
    
    return result
