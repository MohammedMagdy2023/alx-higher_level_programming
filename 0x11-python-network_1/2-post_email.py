#!/usr/bin/python3
"""Create a request to a web server """


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = {
        "email": sys.argv[2],
    }

    # Encode the data
    data = urllib.parse.urlencode(data)
    data = data.encode("UTF-8")

    # Create the request
    url = sys.argv[1]
    req = urllib.request.Request(url, data=data, method="POST")

    # Send the request and get the response
    response = urllib.request.urlopen(req)

    # Print the response content
    print(response.read())
