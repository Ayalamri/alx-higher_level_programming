#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists
if path.exists(filename):
    # Load existing data from the file
    my_list = load_from_json_file(filename)
else:
    # Create an empty list if the file doesn't exist
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
