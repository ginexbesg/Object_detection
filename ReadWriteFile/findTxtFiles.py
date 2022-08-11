# findTxtFiles.py
# Import the argparse library
import argparse
import glob
import os
import shutil
import pathlib

#!python generate_tfrecord.py -x /content/trainingdemo/images/train 

# Create the parser

my_parser = argparse.ArgumentParser(description='Display txt filenames in the images folder')

# Add the arguments to get train/test images folder path
my_parser.add_argument('--x',
                       action='store',
                       type=str,
                       help='the path of images folder')


# Execute the parse_args() method
args = my_parser.parse_args()

imagesFolder_path = args.x


#to display input paths' text
print(imagesFolder_path)

#to make the path from text
path = pathlib.Path(imagesFolder_path)

#get the path 
path.resolve()

#to find txt files under this path folder
pathImages = os.path.join(path.resolve(),'*.txt')
print(pathImages )

#to display all txt files found
for file_name in glob.glob(pathImages):
    print(file_name)

