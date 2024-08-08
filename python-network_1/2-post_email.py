#!/usr/bin/python3
"""doc strings in 2024?"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    """Documented"""
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
