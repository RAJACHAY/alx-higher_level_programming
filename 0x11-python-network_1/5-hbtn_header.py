#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header.
"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get("X-Request-Id"))
