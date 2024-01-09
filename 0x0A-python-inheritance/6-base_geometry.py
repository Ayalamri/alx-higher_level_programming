#!/usr/bin/python3
'''Module for an empty class BaseGeometry.'''


class BaseGeometry:
    '''A class with an unimplemented area method.'''
    
    def area(self):
        '''Raises an Exception with the message area() is not implemented.'''
        raise Exception("area() is not implemented")
