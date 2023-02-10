#!/usr/bin/python3
"""
Load, add, save
"""


import json
import sys
"""Import two modules
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = load_from_json_file('add_item.json')
new_file = save_to_json_file(args + sys.argv[1:], 'add_item.json')
