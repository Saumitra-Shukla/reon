#!/usr/bin/env python3
from yolo_pipeline import *
from lane import *
import numpy as np
import cv2
import os

def pipeline_yolo(img):
    img_undist, img_lane_augmented, lane_info = lane_process(img)
    output = vehicle_detection_yolo(img_undist, img_lane_augmented, lane_info)
    return output


cap = cv2.VideoCapture('./example_data/project_video.mp4')
print(cap)
while(cap.isOpened()):
    ret, frame = cap.read()
    yolo_result = pipeline_yolo(frame)
    cv2.imshow('frame',yolo_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
