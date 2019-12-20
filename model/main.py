#!/usr/env/python3
import matplotlib.image as mpimg
from yolo_pipeline import *
from lane import *

# This function renders the whole image...
def pipeline_yolo(img):
    img_undist, img_lane_augmented, lane_info = lane_process(img)
    output = vehicle_detection_yolo(img_undist, img_lane_augmented, lane_info)
    return output

if __name__ == "__main__":

    demo = 1  # 1:image (YOLO and SVM), 2: video (YOLO Pipeline), 3: video (SVM pipeline)

    if demo == 1:
        import numpy as np
        import cv2

        cap = cv2.VideoCapture('examples/project_video.mp4')

        while(cap.isOpened()):
            ret, frame = cap.read()

            gray = frame
            yolo_result = pipeline_yolo(gray)

            cv2.imshow('frame',yolo_result)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        


