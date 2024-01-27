#!/usr/bin/python3
"""Create a request to a web server """


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as conn:
        resp = conn.read()
        page_type = type(resp)
        utf_content = resp.decode("UTF-8")
        print("Body response:")
        print("\t- type: {}".format(page_type))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(utf_content))
