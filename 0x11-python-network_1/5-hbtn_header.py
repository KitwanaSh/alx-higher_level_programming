#!/usr/bin/python3
""" Takes in a URL, send a request to the URL
    - The ony package to use is 'requests'
    - import also the sys library
"""


import requests, sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
