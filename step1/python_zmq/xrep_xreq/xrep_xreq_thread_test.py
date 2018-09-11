# _*_ coding: utf-8 _*_

"""
python_class.py by hdf
"""

import time
import threading
import zmq
import os


def worker_routine(worker_url, context):
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)
    while True:
        string = socket.recv_string()
        print("Received request: [%s]\n" % string)
        print(threading.current_thread().name)
        time.sleep(1)

        socket.send_string("World")


def main():
    url_worker = "inproc://workers"
    url_client = "tcp://*:5559"

    context = zmq.Context(1)

    clients = context.socket(zmq.XREP)
    clients.bind(url_client)

    workers = context.socket(zmq.XREQ)
    workers.bind(url_worker)

    for i in range(5):
        thread = threading.Thread(target=worker_routine, args=(url_worker, context,))
        thread.start()

    zmq.device(zmq.QUEUE, clients, workers)

    clients.close()
    workers.close()
    context.term()


if __name__ == "__main__":
    main()
