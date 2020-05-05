#!/usr/bin/env python3
# process all images in a directory and put results in another dir
# resize all the images of one dir

import os
import sys
import pyvips

def resize(filein, fileout, maxw, maxh):
    im = pyvips.Image.new_from_file(filein, access="sequential")
    #out = im.resize(factor, kernel = "cubic")
    out = pyvips.Image.thumbnail(filein, maxw, height=maxh)
    out.write_to_file(fileout , Q=95)

# check dir dir args
if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
    # process all from one dir to the other
    srcdir = sys.argv[1]
    dstdir = sys.argv[2]
    files = os.listdir(srcdir)
    for fname in files:
        resize(srcdir + "/" + fname, dstdir + "/" + fname, 1000,200)

else:
    print("args: input dir, outputdir")
	
