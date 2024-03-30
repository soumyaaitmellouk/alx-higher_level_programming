#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    body = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(body)
