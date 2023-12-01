#!/usr/bin/python3
import dis
import marshal
import sys
import types

def get_names_from_code(code):
    names = set()
    for instruction in dis.get_instructions(code):
        if instruction.opcode == dis.opmap['LOAD_NAME']:
            names.add(instruction.argval)
    return names

def get_names_from_module(module_path):
    with open(module_path, 'rb') as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code_object = marshal.load(file)
    return get_names_from_code(code_object)

def print_sorted_names(module_path):
    names = get_names_from_module(module_path)
    sorted_names = sorted(name for name in names if not name.startswith("__"))
    for name in sorted_names:
        print(name)

if __name__ == "__main__":
    if sys.version_info[:2] != (3, 8):
        print("Please run this script using Python 3.8.x.")
    else:
        module_path = "hidden_4.pyc"
        print_sorted_names(module_path)
