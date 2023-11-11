from socket import *
import threading
from _thread import *

from MockSprinkler import MockSprinkler

lock = threading.Lock()

def threaded_server(c):

    while True:

        data = c.recv(1024)

        print(data.decode())

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: text/html\r\n')

        c.send("\r\n".encode())
        c.close()

        lock.release()
        break

    c.close()

def main():

    print('')

    s = socket(AF_INET, SOCK_STREAM)

    s.bind((gethostname(), 12000))

    print(f'Server socket has been created on {s.getsockname()[0]}:12000.\n')

    s.listen(5)

    print(f'Server socket is listening.\n')

    while True:

        c, address = s.accept()

        lock.acquire()

        print(f'Connection established from address {address[0]}:{address[1]}.\n')

        start_new_thread(threaded_server, (c,))

    s.close()

if __name__ == '__main__':

    main()