#!/usr/bin/python3
"""
Function to append a string to the end of a text file and return the number of characters added
"""

def append_write(filename="", text=""):
    """
    Append the given text to the file and return the number of characters added.
    If the file doesn't exist, it will be created.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
