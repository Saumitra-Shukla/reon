#! /usr/bin/env python3 

import os 
basepath = str(os.environ["BASEPATH"])
print("The base path is"+ str(basepath))
# Add the following process here
dprocesses = [
    ["model",basepath+"/model/main.py"]
]
# Dprocesses stand for driving processes

for i in dprocesses:
    print("started process {}".format(i[0]))
    os.system(i[1])

# This above is starting the processes after each other 
# TODO: Engage processes when car is driving and not just standing
