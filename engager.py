import zmq
import time
engageport = 8000
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8000")
while True:
	socket.send(b"engaged")
	time.sleep(1)
	socket.recv()
