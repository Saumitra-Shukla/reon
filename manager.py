#! /usr/env/python3 
import os 
# Processes: [
#  ["Process name", "path_to_start"]
# ]
processes = [
    ["model","./model/main.py"]
]



for i in processes:
    print("Starting process {}".format(i[0]))
    os.system("python3 "+str(i[1]))