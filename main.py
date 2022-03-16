import requests
import sys

print("requests module version:")
print(requests.__version__)

response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)

# Get Python Interpreter version
# 3.10.2 with python3.10 main.py
# 3.9.10 when run with python3.9 
# 3.6.9 when run with python3 
print(sys.version)