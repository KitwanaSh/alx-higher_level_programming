#!/usr/bin/python3
""" Fetaches 'https://alx-intranet.hbtn.io/status' """
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        rep = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(rep)))
        print("\t- content: {}".format(rep))
        print("\t- utf8 content: {}".format(rep.decode(encoding='utf-8')))
