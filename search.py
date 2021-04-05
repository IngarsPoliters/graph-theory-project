# Graph Theory Project GMIT
# Author: Ingars Politers
# G00374677

# This program will allow the user to input the location of a text file
# It will take a regular expression and output the lines matching the expression

import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# Read in path of the file. For WSL use /mnt/c/Users/MyUser/Desktop
# For Windows use C:\Users\MyUser\Desktop
path = input("Please enter folder path e.g. /mnt/c/Users/MyUser/Desktop: ")

# Read in name of the file.
name = input("Please enter text file name: ")

# Find the full path of the file
fullpath = find(name, path)

# Print the full path of file
print(f'The path is {fullpath}')

# Open the file
f = open(fullpath, "r")

# Read whats inside the file
print(f.read())

