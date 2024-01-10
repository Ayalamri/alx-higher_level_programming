#!/usr/bin/python3
"""
Function to read a text file and print to stdout
"""

def read_file(filename=""):
    """
    Read the content of the file and print it to stdout.
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
