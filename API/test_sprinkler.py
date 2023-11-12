""" from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((gethostname(), 12000))

s.send('Ping'.encode())

print(s.recv(1024).decode())

s.close() """

import requests
import json

import time

data = {'function': 'start', 'id': 0}

r1 = requests.post('http://172.18.144.1:12000', data)

time.sleep(17)

data = {'function': 'stop', 'id': 0}

r1 = requests.post('http://172.18.144.1:12000', data)

""" data = {'function': 'add', 'id': 3, 'name': 'Back Yard Flower Sprinkler', 'period': '4', 'seed_type': 3}

r1 = requests.post('http://172.18.144.1:12000', data)

data = {'function': 'add', 'id': 1, 'name': 'Back Yard Flower Sprinkler', 'period': '4', 'seed_type': 3}

r2 = requests.post('http://172.18.144.1:12000', data)

data = {'id': '1'}

r = requests.delete('http://172.18.144.1:12000', headers=data) """

print(r1)