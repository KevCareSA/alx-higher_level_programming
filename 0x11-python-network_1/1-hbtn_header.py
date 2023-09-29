#!/usr/bin/python3

'''
a Python script that takes in a URL, sends a request to the URL
and displays the value
'''

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        headers = resp.headers

    headers = dict(headers)
    print(headers.get("X-Request-Id"))
