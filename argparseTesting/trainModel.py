# imagePath.py
# Import the argparse library
import argparse
import cv2
import numpy as np
import os
import sys

#!python model_main_tf2.py 
#--model_dir=/content/training_demo/models/my_ssd_resnet101_v1_fpn 
#--pipeline_config_path=/content/training_demo/models/my_ssd_resnet101_v1_fpn/pipeline.config
# Create the parser

my_parser = argparse.ArgumentParser(description='Train model getting model folder and pipeline.config')

# Add the arguments to get the path of model folder
my_parser.add_argument('--model_dir',
                       action='store',
                       type=str,
                       help='the path of model folder')

# Add the arguments to get the path of pipeline.config file
my_parser.add_argument('--pipeline_config_path',
                       action='store',
                       type=str,
                       help='the path of pipeline.config file')


# Execute the parse_args() method
args = my_parser.parse_args()

model_path = args.model_dir
configFile_path = args.pipeline_config_path

print('model path is ',(model_path))
print('config_path is ',(configFile_path))

