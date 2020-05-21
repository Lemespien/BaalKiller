""" Holds all image references """
from os import listdir
from os.path import isfile, join

IMAGE_FOLDER = "images/"
FILES = [f for f in listdir(IMAGE_FOLDER) if isfile(join(IMAGE_FOLDER, f))]
IMAGE_DICTIONARY = {}
for file in FILES:
    IMAGE_DICTIONARY[file.split(".")[0]] = IMAGE_FOLDER + file
