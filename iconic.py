#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os
import shutil

from PIL import Image

def makeDPI(icon):
    im = Image.open(icon)
    (x, y) = im.size
     
    mdpi = (int(x*0.25), int(y*0.25))
    hdpi = (int(x*0.375), int(y*0.375))
    xhdpi = (int(x*0.5), int(y*0.5))
    xxhdpi = (int(x*0.75), int(y*0.75))
    xxxhdpi = (x, y)
     
    mdpi_im = im.resize(mdpi, Image.ANTIALIAS)
    mdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-mdpi/" + os.path.basename(icon))
     
    hdpi_im = im.resize(hdpi, Image.ANTIALIAS)
    hdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-hdpi/" + os.path.basename(icon))
      
    xhdpi_im = im.resize(xhdpi, Image.ANTIALIAS)
    xhdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-xhdpi/" + os.path.basename(icon))
      
    xxhdpi_im = im.resize(xxhdpi, Image.ANTIALIAS)
    xxhdpi_im.save(os.path.dirname(os.path.abspath(icon)) + "/drawable-xxhdpi/" + os.path.basename(icon))
# end

dir = sys.argv[1]
names = os.listdir(dir) # List of files and directories
for name in names:
    fullname = os.path.join(dir, name) # getting full name
    if os.path.isfile(fullname): # if it is a file...
        print "Converting: " + os.path.basename(fullname)
        makeDPI(fullname)
    # end
# end
