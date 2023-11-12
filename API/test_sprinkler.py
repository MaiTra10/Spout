""" from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((gethostname(), 12000))

s.send('Ping'.encode())

print(s.recv(1024).decode())

s.close() """

import requests

data = {'function': 'add', 'id': 3, 'name': 'Back Yard Flower Sprinkler', 'period': '4', 'seed_type': 3}

r = requests.post('http://10.14.101.143:12000', data)

data = {'function': 'add', 'id': 1, 'name': 'Back Yard Flower Sprinkler', 'period': '4', 'seed_type': 3}

r = requests.post('http://10.14.101.143:12000', data)

data = {'id': '1'}

r = requests.delete('http://10.14.101.143:12000', headers=data)

print(r.content)