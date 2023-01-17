#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays
the body of the response
"""


from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
