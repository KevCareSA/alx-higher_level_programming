#!/usr/bin/python3
""" a text file reading funcion."""


def read_file(filename=""):
    """Print the UTF8 contents text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
