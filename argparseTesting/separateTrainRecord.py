# imagePath.py
# Import the argparse library
import argparse
import cv2
import numpy as np
import os
import sys

#!python generate_tfrecord.py 
#-x /content/trainingdemo/images/train 
#-l /content/trainingdemo/annotations/label_map.pbtxt 
#-o /content/trainingdemo/annotations/train.record
# Create the parser

my_parser = argparse.ArgumentParser(description='Create train record using train images and labels')

# Add the arguments to get train/test images folder path
my_parser.add_argument('--x',
                       action='store',
                       type=str,
                       help='the path of images folder')
# Add the arguments to get train/test label map pbtxt file path
my_parser.add_argument('--l',
                       action='store',
                       type=str,
                       help='the path of label map txt file')
# Add the arguments to set  output record path of train/test  
my_parser.add_argument('--o',
                       action='store',
                       type=str,
                       help='the path to save train record file')

# Execute the parse_args() method
args = my_parser.parse_args()

imagesFolder_path = args.x
label_path = args.l
outputSavingRecord_path = args.o


print(imagesFolder_path)
print(label_path)
print(outputSavingRecord_path)
