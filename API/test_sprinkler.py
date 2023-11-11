""" from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((gethostname(), 12000))

s.send('Ping'.encode())

print(s.recv(1024).decode())

s.close() """

import requests

data = {'function': 'add', 'id': 0, 'name': 'Front Yard Flower Sprinkler', 'timer_mode': 'Auto', 'seed_type': 0}

r = requests.post('http://10.14.101.143:12000', data)

print(r)