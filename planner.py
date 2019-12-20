import os
import zmq 
from message import *

while True:

	messageserver = MessengerServer(8000)

	if recieve(messageserver) == 1:
		print("Engaging now")


