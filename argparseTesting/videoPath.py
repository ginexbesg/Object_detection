# imagePath.py
# Import the argparse library
import argparse
import cv2
import numpy as np
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Image path')

# Add the arguments
my_parser.add_argument('--video',
                       action='store',
                       type=str,
                       help='the path to dispaly video')

# Execute the parse_args() method
args = my_parser.parse_args()

video_path = args.video
print(video_path)
cap = cv2.VideoCapture(video_path)
while True:
    _, img= cap.read()
    height, width, _ = img.shape
    cv2.imshow('Image',img)
    key = cv2.waitKey(1)
    if key==27:
        break


cv2.destroyAllWindows()