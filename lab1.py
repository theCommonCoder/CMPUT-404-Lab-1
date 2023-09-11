import requests

print("requests version:", requests.__version__)

r = requests.get('https://www.google.com')

print()
print(r.content.decode("utf8"))
