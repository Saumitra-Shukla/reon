# Import this to use ZMQ messaging
import os 
import zmq 


def MessengerServer(port):
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://*:"+str(port))
	return socket
def MessengerClient(port):
	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://localhost:"+str(port))
	return socket
def recieve(socket):
	message = socket.recv()
	return message

def send(socket, message):
	socket.send_string(message)
	pass 

