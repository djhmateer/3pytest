import requests
import sys

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

# 3.10.2 with python3.10 main.py
# 3.9.10 when run with python3.9 
# 3.6.9 when run with python3 
print(sys.version)