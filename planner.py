import zmq 
import os 
import time
BASEPATH = str(os.environ["BASEPATH"])

# Engage Port 8000 is used here
def engagecheck():
	engageport = 8000
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://*:"+str(engageport))
	message = socket.recv()
  #	ZMQ requires an answer, even though we dont send anything, we need to reply to the client, else ZMQ will spit out error s and the programm won't move on
	socket.send(b"")	
	return message
	
while True:
	while engagecheck()  == b"engaged":
		print("Model is engaged")
	

