#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    requ = requests.get(argv[1])
    status = requ.status_code
    print(requ.text) if status < 400 else print(
        "Error code: {}".format(requ.status_code))
