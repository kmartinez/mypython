#!/usr/bin/env python3
# print avg for all images in a dir

import os
import sys
import pyvips

d = sys.argv[1]
for filename in os.listdir(d) :
    im = pyvips.Image.new_from_file(d + "/" + filename, access="sequential")
    print(filename + ": " + str(im.max()))

