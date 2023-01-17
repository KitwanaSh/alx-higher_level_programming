#!/usr/bin/python3
""" feteches 'https://alx-internet.hbtn.io/status'
by using only the package requests
"""


import requests

if __name__ == "__main__":
	req = requests.get("https://alx-intranet.hbtn.io/status")
	print("Body response:")
	print("\t- type: {}".format(type(req.text)))
	print("\t- content: {}".format(req.text))
