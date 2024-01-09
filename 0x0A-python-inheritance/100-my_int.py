#!/usr/bin/python3
"""
the class MyInt
"""


class MyInt(int):
    """version of an inte"""
    def __new__(cls, *args, **kwargs):
        """new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """was != is =="""
        return int(self) != other

    def __ne__(self, other):
        """was == is !="""
        return int(self) == other
