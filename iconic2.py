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
    # end

# end

def makeDPI(icon):
    im = Image.open(icon)
    (x, y) = im.size
     
    mdpi = (int(x*0.25), int(y*0.25))
    hdpi = (int(x*0.375), int(y*0.375))
    xhdpi = (int(x*0.5), int(y*0.5))
    xxhdpi = (int(x*0.75), int(y*0.75))
    xxxhdpi = (x, y)
     
    mdpi_im = im.resize(mdpi, Image.ANTIALIAS)
    # The line below inserts drawable-*dpi into path, where generated icons are stored.
    mdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-mdpi/" + os.path.basename(icon))
     
    hdpi_im = im.resize(hdpi, Image.ANTIALIAS)
    hdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-hdpi/" + os.path.basename(icon))
      
    xhdpi_im = im.resize(xhdpi, Image.ANTIALIAS)
    xhdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-xhdpi/" + os.path.basename(icon))
      
    xxhdpi_im = im.resize(xxhdpi, Image.ANTIALIAS)
    xxhdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-xxhdpi/" + os.path.basename(icon))
# end

def printHelpMessage():
    print "iconic2 is  a simple tool that generates icons for different dpi in android projects."
    print " "
    print "Usage:"
    print "iconic2.py /path/to/xxxhdpi/icons/"
    print " "
    print "-help : Displays this help message"
# end


def main():
    
    if len(sys.argv) == 2: # If there are two arguments: argv[0] and argv[1]
        if sys.argv[1] == "-help": # And if this one is -help
            printHelpMessage()
            exit()
        else: # If not -help
            if os.path.isdir(sys.argv[1]): # And if such a directory really exists
                dir = sys.argv[1] # Go further and convert icons
            else:
                print sys.argv[1] + " is not a directory or doesn't exist."
                exit()
    else: # If there is something strange
        print "Usage: iconic2.py /path/to/xxxhdpi/icons/" # Just show help
        exit()
    
    createDirs(dir)
    names = os.listdir(dir) # List of files and directories
    for name in names:
        fullname = os.path.join(dir, name) # Getting full name
        if os.path.isfile(fullname): # If it is a file...
            print "Processing: " + os.path.basename(fullname)
            makeDPI(fullname)
        #end
    # end
# end

main()