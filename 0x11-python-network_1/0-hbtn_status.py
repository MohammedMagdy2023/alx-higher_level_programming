#!/usr/bin/python3
"""Create a request to a web server """
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as conn:
    resp = conn.read()
    page_type = type(resp)
    utf_content = resp.decode("UTF-8")
    print(f"""Body response:
    - type: {page_type}
    - content: {resp}
    - utf8 content: {utf_content}""")
