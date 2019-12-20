#! /usr/bin/env python3 
import os 
import time 
import zmq
basepath = str(os.environ["BASEPATH"])

def engager():
	engageport = 8000
	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://localhost:8000")
	while True:
		socket.send(b"engaged")
		time.sleep(1)
		socket.recv()
	pass
print("The base path is"+ str(basepath))
# TODO: This need to move into planner. See more line 30
# Add the following process here
dprocesses = [
    ["model",basepath+"/model/main.py"]
]
# Dprocesses stand for driving processes

for i in dprocesses:
    print("started process {}".format(i[0]))
    os.system(i[1])


# This function should the planner trigger and planner triggers the model 
engager()


# This above is starting the processes after each other 
# TODO: Engage processes when car is driving and not just standing
