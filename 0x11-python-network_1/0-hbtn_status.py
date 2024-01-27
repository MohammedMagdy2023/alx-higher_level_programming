#!/usr/bin/python3
"""Create a request to a web server """


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as conn:
        resp = conn.read()
        page_type = type(resp)
        utf_content = resp.decode("UTF-8")
        print(f"""Body response:
        - type: {page_type}
        - content: {resp}
        - utf8 content: {utf_content}""")
