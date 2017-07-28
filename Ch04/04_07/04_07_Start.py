# HTTP Package
import urllib.request
import json
import textwrap

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
# https://api.douban.com/v2/book/1220562

with urllib.request.urlopen("https://api.douban.com/v2/book/27001119") as f:
    text = f.read()
    decodeText = text.decode("utf-8")
    print(textwrap.fill(decodeText,width=60))

print()

obj = json.loads(decodeText)
print(obj['title'])
print(obj['author'][1])
