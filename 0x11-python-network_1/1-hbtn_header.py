#!/usr/bin/python3
"""

This is a script that takes in a URL, sends a reqeust to the URL
and displays the value of the X-Request-Id variable found in the
header of the response

"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.getheader('X-Request-Id')
    if headers:
        print(headers)
