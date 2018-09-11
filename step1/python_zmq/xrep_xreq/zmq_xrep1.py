from time import sleep

import zmq

context = zmq.Context()
socket = context.socket(zmq.DEALER)
ident = b'1'
socket.setsockopt(zmq.IDENTITY, ident)
socket.connect("tcp://localhost:5560")

while True:
    message = socket.recv()
    print("rep1 Received request: ")
    print(message.decode('ascii'))

    send_data = "rep1" + " rep msg:"
    socket.send(send_data.encode())
    # message = socket.recv_multipart()
    # print("rep1 Received request: ")
    # for part in message:
    #     print(part.decode('ascii'))
    # send_data = "rep1" + " rep msg:"
    # send_ident = b'req0'
    # socket.send_multipart([send_ident, send_data.encode()])
