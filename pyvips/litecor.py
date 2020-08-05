#!/usr/bin/python3
# by John Cupitt, Aug 2020
import sys
import os
import pyvips

if len(sys.argv) < 3:
    print(f"usage: {sys.argv[0]} grey-card-image image1 image2 ...")
    print(f"   light-correct a set of images with a grey card")
    print(f"   corrected images writtem to lc_image1, lc_image2, etc.")
    sys.exit(1)

# Notes:
# - the grey-card image can have quite a lot of dirt and scratches, so we must
#   do quite a severe low-pass filter
# - for speed, we low-pass filter by downsizing and upsizing again .. the
#   libvips downsizer is high-quality
# - we assume the grey-card image is using the sRGB gamma, so converting to 
#   scRGB will give us a linear light image
# - just use the green channel

print(f"computing correction map ...")
grey = pyvips.Image.new_from_file(sys.argv[1], access="sequential")
largest_feature = 100
small_grey = grey \
    .colourspace("scrgb")[1] \
    .resize(1 / largest_feature) \
    .copy_memory()

# turn to a 0-1 correction factor
small_flatfield = small_grey.max() / small_grey

# size back up to the original dimensions ready to use as a correction field
flatfield = small_flatfield.resize(grey.width / small_flatfield.width,
        vscale=grey.height / small_flatfield.height)

# save for reuse
flatfield = flatfield.copy_memory()

# correct other images
for filename in sys.argv[2:]:
    # to scRGB (linear RGB) for correction, then back for write
    image = pyvips.Image.new_from_file(filename, access="sequential")
    scrgb = image.colourspace("scrgb")
    scrgb *= flatfield
    image = scrgb.colourspace(image.interpretation)
    head, tail = os.path.split(filename)
    new_name = f"{head}lc_{tail}"
    print(f"writing {new_name} ...")
    image.write_to_file(new_name)
    
