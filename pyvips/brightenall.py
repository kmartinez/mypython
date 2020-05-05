#!/usr/bin/env python3
# process all images in a directory and put results in another dir

import os
import sys
import pyvips

def brighten(filein, fileout):
    im = pyvips.Image.new_from_file(filein, access="sequential")
    im *= [2, 2, 2]
    # make jpg but with high quality
    im.write_to_file(fileout , Q=97)

# check dir dir args
if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
    # process all from one dir to the other
    srcdir = sys.argv[1]
    dstdir = sys.argv[2]
    files = os.listdir(srcdir)
    for fname in files:
        brighten(srcdir + "/" + fname, dstdir + "/" + fname)

else:
    print("args: input dir, outputdir")
	
