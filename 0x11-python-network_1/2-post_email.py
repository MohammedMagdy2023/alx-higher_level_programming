#!/usr/bin/python3
"""Create a request to a web server """


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    data = {'email' : sys.argv[2]}

    params = urllib.parse.urlencode(data)
    params = params.encode('ascii') # data should be bytes
    req = urllib.request.Request(sys.argv[1], params)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
