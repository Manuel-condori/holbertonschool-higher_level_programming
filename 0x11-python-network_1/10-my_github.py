#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(argv[1], argv[2]))
    if response.status_code == 200:
        dictio = response.json()
        print(dictio['id'])
    else:
        print(None)
