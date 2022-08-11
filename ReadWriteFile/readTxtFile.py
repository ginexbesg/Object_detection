# writeTxtFile.py
# Import the argparse library
import argparse
import glob
import os
import shutil
import pathlib

#!python generate_tfrecord.py 
#-x /content/trainingdemo/images/train 
#-o /content/trainingdemo/images/train/train.txt
# Create the parser

my_parser = argparse.ArgumentParser(description='write txt file names into txt file')

# Add the arguments to get train/test images folder path
my_parser.add_argument('--x',
                       action='store',
                       type=str,
                       help='the path of images folder')

# Add the arguments to write file names into txt file 
my_parser.add_argument('--o',
                       action='store',
                       type=str,
                       help='the file path to write txt filenames')

# Execute the parse_args() method
args = my_parser.parse_args()

imagesFolder_path = args.x
outputSavingRecord_path = args.o

#to display input paths' text
print(imagesFolder_path)
#print(outputSavingRecord_path)

#to make the path from text
path = pathlib.Path(imagesFolder_path)

#get the path 
path.resolve()

#to find txt files under this path folder
pathImages = os.path.join(path.resolve(),'*.txt')
print(pathImages)


#to display all txt files found
with open(outputSavingRecord_path, mode="w") as file:
    for file_name in glob.glob(pathImages):
        file.write(file_name+'\n')
       
	    