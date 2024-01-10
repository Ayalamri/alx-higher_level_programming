#!/usr/bin/python3
"""
Function to write a string to a text file and return the number of characters written
"""

def write_file(filename="", text=""):
    """
    Write the given text to the file and return the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters
