#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

from PIL import Image

def createDirs(path):
    
    Dirs = ["drawable-mdpi", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi"]
    
    for current_path in Dirs:
        try:
            os.mkdir(path + current_path, 0755)
        except OSError:
            print "Directory " + current_path + " is already exists"

def makeDPI(icon):
    im = Image.open(icon)
    (x, y) = im.size

    sizes_list = {
        'mdpi': (int(x*0.25), int(y*0.25)),
        'hdpi':(int(x*0.375), int(y*0.375)),
        'xhdpi':(int(x*0.5), int(y*0.5)),
        'xxhdpi':(int(x*0.75), int(y*0.75)),
        'xxxhdpi':(x, y)
    }

    for size_name in sizes_list:
        size_im = im.resize(sizes_list[size_name], Image.ANTIALIAS)
        # The line below inserts drawable-*dpi into path, where generated icons are stored.
        size_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-"+size_name+"/" + os.path.basename(icon))

def printHelpMessage(arg=False):

    msg = u"""iconic2 is  a simple tool that generates icons for different dpi in android projects.\n
Usage:\n
iconic2.py /path/to/xxxhdpi/icons/\n\n"""

    if arg:
        msg+="-help : Displays this help message"
    exit()

def printDirErrorMessage():
    print sys.argv[1] + " is not a directory or doesn't exist."
    exit()

def main():
    
    if (len(sys.argv) == 2): # If there are two arguments: argv[0] and argv[1]
        if (sys.argv[1] == "-help"): # And if this one is -help
            printHelpMessage(True)
        else: # If not -help
            # And if such a directory really exists go further and convert icons
            dir = sys.argv[1] if (os.path.isdir(sys.argv[1])) else printDirErrorMessage
    else: # If there is something strange
        printHelpMessage() # Just show help
    
    createDirs(dir)
    names = os.listdir(dir) # List of files and directories
    for name in names:
        fullname = os.path.join(dir, name) # Getting full name
        if (os.path.isfile(fullname)): # If it is a file...
            print "Processing: " + os.path.basename(fullname)
            makeDPI(fullname)



if __name__ == '__main__':
    main()