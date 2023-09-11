import requests

print("requests version:", requests.__version__)

r = requests.get('https://raw.githubusercontent.com/theCommonCoder/CMPUT-404-Lab-1/master/lab1.py')

print()
print(r.content.decode("utf8"))