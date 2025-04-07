import requests
from requests.auth import HTTPBasicAuth

auth=HTTPBasicAuth('username', 'password')

response=requests.get('https://api.github.com/user', auth=auth)