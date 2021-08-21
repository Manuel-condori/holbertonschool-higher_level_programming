#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    content = response.read()
    utf = content.decode('utf-8')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: \
{}".format(type(content), content, utf))
