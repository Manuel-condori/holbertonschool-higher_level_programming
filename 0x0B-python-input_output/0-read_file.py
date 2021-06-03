#!/usr/bin/python3
"""Module that holds a function that reads a file"""


def read_file(filename=""):
    """Args:
        filename: the file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
