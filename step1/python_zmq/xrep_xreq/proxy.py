import zmq


def main():
    context = zmq.Context(1)

    frontend = context.socket(zmq.ROUTER)
    frontend.bind("tcp://*:5559")

    backend = context.socket(zmq.ROUTER)
    backend.bind("tcp://*:5560")

    # zmq.proxy(frontend, backend)
    zmq.device(zmq.QUEUE, frontend, backend)

    while True:
        pass

    frontend.close()
    backend.close()
    context.term()


if __name__ == "__main__":
    main()

# import zmq
#
# context = zmq.Context()
# frontend = context.socket(zmq.XREP)
# backend = context.socket(zmq.XREQ)
# frontend.bind("tcp://*:5559")
# backend.bind("tcp://*:5560")
#
# poller = zmq.Poller()
# poller.register(frontend, zmq.POLLIN)
# poller.register(backend, zmq.POLLIN)
#
# while True:
#     socks = dict(poller.poll())
#
#     if socks.get(frontend) == zmq.POLLIN:
#         message = frontend.recv()
#         more = frontend.getsockopt(zmq.RCVMORE)
#         if more:
#             backend.send(message, zmq.SNDMORE)
#         else:
#             backend.send(message)
#
#     if socks.get(backend) == zmq.POLLIN:
#         message = backend.recv()
#         more = backend.getsockopt(zmq.RCVMORE)
#         if more:
#             frontend.send(message, zmq.SNDMORE)
#         else:
#             frontend.send(message)
