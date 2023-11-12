""" from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((gethostname(), 12000))

s.send('Ping'.encode())

print(s.recv(1024).decode())

s.close() """

import requests
import time

print(' ')

data = {'function': 'add', 'id': 3, 'name': 'Back Yard Flower Sprinkler', 'period': '4', 'seed_type': 3}

r1 = requests.post('http://172.18.144.1:12000', data)

print(r1.content.decode('utf-8'))

r1 = requests.get('http://172.18.144.1:12000')

print(r1.content.decode('utf-8'))

data = {'function': 'add', 'id': 1, 'name': 'Front Yard Flower Sprinkler', 'period': '2', 'seed_type': 2}

r2 = requests.post('http://172.18.144.1:12000', data)

print(r2.content.decode('utf-8'))

data = {'function': 'start', 'id': 1}

r1 = requests.post('http://172.18.144.1:12000', data)

data = {'function': 'start', 'id': 3}

r2 = requests.post('http://172.18.144.1:12000', data)

time.sleep(5)

data = {'function': 'stop', 'id': 1}

r1 = requests.post('http://172.18.144.1:12000', data)

print(r1.content.decode('utf-8'))

time.sleep(12)

data = {'function': 'stop', 'id': 3}

r1 = requests.post('http://172.18.144.1:12000', data)

print(r1.content.decode('utf-8'))

data = {'id': 3}

r1 = requests.delete('http://172.18.144.1:12000', params=data)

print(r1.content.decode('utf-8'))

data = {'id': 1, 'seed_type': 5}

r1 = requests.put('http://172.18.144.1:12000', data)

print(r1.content.decode('utf-8'))