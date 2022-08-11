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
my_parser.add_argument('--image',
                       action='store',
                       type=str,
                       help='the path to show image')

# Execute the parse_args() method
args = my_parser.parse_args()

image_path = args.image
print(image_path)
img= cv2.imread(image_path)
height, width, _ = img.shape
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()