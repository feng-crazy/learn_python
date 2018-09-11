from time import sleep

import zmq

context = zmq.Context()
socket = context.socket(zmq.DEALER)
ident = b'0'
socket.setsockopt(zmq.IDENTITY, ident)
socket.connect("tcp://localhost:5559")
request = 0
while True:
    request = request + 1
    send_data = "req1" + " request:" + str(request)
    socket.send(send_data.encode())
    message = socket.recv()
    print(message.decode('ascii'))
    sleep(1)

    # request = request + 1
    # send_data = "req1" + " request:" + str(request)
    # send_ident = b'rep0'
    # socket.send_multipart([send_ident, send_data.encode()])
    # message = socket.recv_multipart()
    # print("Received reply ", request)
    # for part in message:
    #     print(part.decode('ascii'))
    # sleep(1)
