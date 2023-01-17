#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
and display the value of the 'X-request-Id'

Should change the id for every try
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        print(dict(response.headers).get("X-Request-Id"))
