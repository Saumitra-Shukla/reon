#!/usr/bin/env python3
from yolo_pipeline import *
from lane import *
import numpy as np
import cv2
import os
basepath = str(os.environ["BASEPATH"])
print("The base path is"+ str(basepath))

def pipeline_yolo(img):
    img_undist, img_lane_augmented, lane_info = lane_process(img)
    output = vehicle_detection_yolo(img_undist, img_lane_augmented, lane_info)
    return output


# In the end product the actual capturing should happen
cap = cv2.VideoCapture(basepath+'/model/example_data/project_video.mp4')
print(cap)
while (cv2.waitKey(1) != ord('q')):
    ret, frame = cap.read()
    
    frame = cv2.resize(frame,(1280,720))
    yolo_result = pipeline_yolo(frame)
    cv2.imshow('frame',yolo_result)
    
cap.release()
cv2.destroyAllWindows()
