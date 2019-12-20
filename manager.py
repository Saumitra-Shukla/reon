#! /usr/bin/env python3 

import os 
basepath = str(os.environ["BASEPATH"])
print("The base path is"+ str(basepath))
processes = [
    ["model",basepath+"/model/main.py"]
]

for i in processes:
    print("started process {}".format(i[0]))
    os.system(i[1])

# This above is starting the processes after each other 
# TODO: Engage processes when car is driving and not just standing
