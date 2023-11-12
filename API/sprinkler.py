import threading
import simplejson as json
from datetime import datetime
from socket import *
from _thread import *

from MockSprinkler import MockSprinkler

lock = threading.Lock()

sprinklers = []

def create_client_response(response):

    try:

        return (
            
            f'HTTP/1.1 {response["status"]} {response["msg"]}\r\n'
            f'Content-Type: text/html\r\n\r\n'
            f'{(response["content"])}\r\n'

        )
    
    except:

        return (
            f'HTTP/1.1 {response["status"]} {response["msg"]}\r\n'

        )

def get_handler(c, function):

    if function == 'get':

        all_sprinkler_data = []

        for sprinkler in sprinklers:

            all_sprinkler_data.append(str(sprinkler))

        response =  {

            'status': 200,
            'msg': 'OK',
            'content': json.dumps(all_sprinkler_data)

        }
    
    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }

    client_response = create_client_response(response).encode()

    c.send(client_response)

def post_handler(c, function, data):

    if function == 'add':

        values = data[-1].split('&')[1:]

        sid = values[0].split('=')[1]

        name = values[1].split('=')[1].replace('+', ' ')

        period = values[2].split('=')[1]

        seed_type = values[3].split('=')[1]
        
        sprinklers.append(MockSprinkler(sid, name, period, seed_type))

        response =  {

            'status': 200,
            'msg': 'OK',
            'content':f'Sprinkler with ID {sid} named {name} has been successfully added! {str(sprinklers[-1])}'

        }

    elif function == 'start':

        index = get_index_from_id(data[-1].split('&')[1].split('=')[1])

        sprinklers[index].set_previous_start_time()
        sprinklers[index].set_status(True)

        response =  {

            'status': 200,
            'msg': 'OK',
            'content': f'Sprinkler with ID {data[-1].split("&")[1].split("=")[1]} has started!'

        }

    elif function == 'stop':

        index = get_index_from_id(data[-1].split('&')[1].split('=')[1])

        sprinkler = sprinklers[index]

        time_now = datetime.now()

        total_seconds_now = time_now.hour * 3600 + time_now.minute * 60 + time_now.second
        total_seconds_then = sprinkler.get_previous_start_hour() * 3600 + sprinkler.get_previous_start_min() * 60 + sprinkler.get_previous_start_sec()
        
        time_diff = total_seconds_now - total_seconds_then

        timings = {'hours': time_diff // 3600, 'minutes': (time_diff % 3600) // 60, 'seconds': time_diff % 60}

        sprinkler.set_previous_run_time(timings)

        sprinkler.set_status(False)

        response =  {

            'status': 200,
            'msg': 'OK',
            'content': f'Sprinkler with ID {data[-1].split("&")[1].split("=")[1]} has been stopped. It took: {str(timings)}'

        }

    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }

    client_response = create_client_response(response).encode()

    c.send(client_response)

def get_index_from_id(sid):

    index_counter = 0

    for sprinkler in sprinklers:

        if int(sprinkler.get_id()) == int(sid):

            break
        
        index_counter += 1

    return index_counter

def delete_handler(c, function, data):

    if function == 'remove':        

        index_counter = get_index_from_id(data[1].split('=')[1])

        del sprinklers[index_counter]

        response =  {

            'status': 200,
            'msg': 'OK',
            'content': f'Sprinkler with ID {data[1].split("=")[1]} has been deleted!'

        }

    else:

        response =  {

            'status': 400,
            'msg': 'Bad Request'

        }

    client_response = create_client_response(response).encode()

    c.send(client_response)

def put_handler(c, function, data):

    if function == 'update':

        index = data[-1].split('&')[0].split('=')[1]

        if data[-1].split('&')[1].split('=')[0] == 'auto_status':

            index = get_index_from_id(index)

            sprinklers[index].set_if_sprinkler_timer_auto(bool(data[-1].split('&')[1].split('=')[1]))

        elif data[-1].split('&')[1].split('=')[0] == 'name':

            index = get_index_from_id(index)

            sprinklers[index].set_sprinkler_name(str(data[-1].split('&')[1].split('=')[1]))

        elif data[-1].split('&')[1].split('=')[0] == 'period':

            index = get_index_from_id(index)

            sprinklers[index].set_period(int(data[-1].split('&')[1].split('=')[1]))

        elif data[-1].split('&')[1].split('=')[0] == 'seed_type':

            index = get_index_from_id(index)

            sprinklers[index].set_seed_type(int(data[-1].split('&')[1].split('=')[1]))

        elif data[-1].split('&')[1].split('=')[0] == 'status':

            index = get_index_from_id(index)

            sprinklers[index].set_status(bool(data[-1].split('&')[1].split('=')[1]))

        response =  {

            'status': 200,
            'msg': 'OK',
            'content': str(sprinklers[index])

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

    elif data[0] == 'GET':

        function = 'get'

    else:

        function = data[-1].split('&')[0].split('=')[1]

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

            delete_handler(c, function, data)

        elif request_type == 'PUT':

            put_handler(c, function, data)

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