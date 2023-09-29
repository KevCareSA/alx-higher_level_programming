#!/usr/bin/python3
"""
a script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    requ = requests.get(url)
    text = requ.text
    print("Body response:")
    print(f"\t- type: {type(text)}")
    print(f"\t- content: {text}")
