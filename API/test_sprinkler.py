""" from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((gethostname(), 12000))

s.send('Ping'.encode())

print(s.recv(1024).decode())

s.close() """

import requests

data = {'test': 'item'}

r = requests.get('http://10.14.101.143:12000', data)

print(r.content)