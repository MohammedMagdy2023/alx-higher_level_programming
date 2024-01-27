#!/usr/bin/python3
"""Create a request to a web server """
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(url = sys.argv[1]) as conn:
        print(dict(conn.headers).get("X-Request-Id"))
