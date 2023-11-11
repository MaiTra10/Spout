from socket import *
import threading
from _thread import *
import simplejson as json

#from MockSprinkler import MockSprinkler

lock = threading.Lock()

sprinklers = []

def create_client_response(response):

    try:

        return (
            f'HTTP/1.1 {response["status"]} {response["msg"]}\r\n'
            f'Content-Type: application/json\r\n'
            f'Content-length: {len(response["content"])}\r\n'
            '\r\n'
            f'{json.dumps(response["data"])}'

        )
    
    except:

        return (
            f'HTTP/1.1 {response["status"]} {response["msg"]}\r\n'

        )

def get_handler(c, function):

    if function == 'get':

        response =  {

            'status': 200,
            'msg': 'OK'

        }
    
    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }

    client_response = create_client_response(response).encode()

    c.send(client_response)

def post_handler(c, function, data):

    """
    self.sprinkler_id = 0
    self.sprinker_name = None
    self.sprinkler_timer_mode = None # Auto or Manual
    self.schedule = []
    self.seed_type = seed_type
    self.status = False
    self.previous_run_time = None
    self.previous_start_time = None
    """

    if function == 'add':

        print(data)

        response =  {

            'status': 200,
            'msg': 'OK'

        }

    elif function == 'start':

        response =  {

            'status': 200,
            'msg': 'OK'

        }

    elif function == 'stop':

        response =  {

            'status': 200,
            'msg': 'OK'

        }

    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }

    client_response = create_client_response(response).encode()

    c.send(client_response)

def delete_handler(c, function):

    if function == 'remove':        

        response =  {

            'status': 200,
            'msg': 'OK'

        }

    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }

    client_response = create_client_response(response).encode()

    c.send(client_response)

def put_handler(c, function):

    if function == 'update':

        response =  {

            'status': 200,
            'msg': 'OK'

        }

    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }
        
    client_response = create_client_response(response).encode()

    c.send(client_response)

def get_function(data):

    if data[0] == 'DELETE':

        function = 'remove'

    elif data[0] == 'PUT':

        function = 'update'

    else:

        if data[1] == '/':

            function = data[-1].split('=')[1]

        else:

            function = data[1].split('=')[1]

    return function

def threaded_server(c):

    while True:

        data = c.recv(1024).decode().split()

        request_type = data[0]

        function = get_function(data)

        if request_type == 'GET':

            get_handler(c, function)

        elif request_type == 'POST':

            post_handler(c, function, data)

        elif request_type == 'DELETE':

            delete_handler(c, function)

        elif request_type == 'PUT':

            put_handler(c, function)

        else:

            client_response = create_client_response({'status': 400,'msg': 'Bad Request'})

            c.send(client_response.encode())

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