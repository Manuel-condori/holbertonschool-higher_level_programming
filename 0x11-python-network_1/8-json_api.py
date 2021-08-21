#!/usr/bin/python3
"""
Script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    values = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        result = r.json()
        if result:
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
