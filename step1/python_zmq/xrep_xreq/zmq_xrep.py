from time import sleep

import zmq

context = zmq.Context()
socket = context.socket(zmq.DEALER)
ident = b'0'
socket.setsockopt(zmq.IDENTITY, ident)
socket.connect("tcp://localhost:5560")

while True:
    message = socket.recv()
    print("rep0 Received request: ")
    print(message.decode('ascii'))

    send_data = "rep0" + " rep msg:"
    socket.send(send_data.encode())
    # message = socket.recv_multipart()
    # print("rep0 Received request: ")
    # for part in message:
    #     print(part.decode('ascii'))
    # send_data = "rep0" + " rep msg:"
    # send_ident = b'req1'
    # socket.send_multipart([send_ident, send_data.encode()])
