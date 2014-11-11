#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PIL import Image

im = Image.open(sys.argv[1])
(x, y) = im.size

mdpi = (int(x*0.25), int(y*0.25))
hdpi = (int(x*0.375), int(y*0.375))
xhdpi = (int(x*0.5), int(y*0.5))
xxhdpi = (int(x*0.75), int(y*0.75))
xxxhdpi = (x, y)

mdpi_im = im.resize(mdpi, Image.ANTIALIAS)
mdpi_im.save("MDPI-"+sys.argv[1]);

hdpi_im = im.resize(hdpi, Image.ANTIALIAS)
hdpi_im.save("HDPI-"+sys.argv[1]);

xhdpi_im = im.resize(xhdpi, Image.ANTIALIAS)
xhdpi_im.save("XHDPI-"+sys.argv[1]);

xxhdpi_im = im.resize(xxhdpi, Image.ANTIALIAS)
xxhdpi_im.save("XXHDPI-"+sys.argv[1]);
