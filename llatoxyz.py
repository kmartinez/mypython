# convert lla to xyz
# we list as lon lat alt
import pyproj
from math import sqrt

lon0, lat0, alt0 = {-16.424020795,  64.013078821, 31.473}
lon, lat, alt = {-16.424020922,  64.013078898, 31.483}

def geodetic_to_cartesian(longitude, latitude, altitude):
    # Define the input and output coordinate systems
    input_crs = pyproj.CRS("EPSG:4326")  # WGS84 geodetic coordinates
    output_crs = pyproj.CRS("EPSG:4978")  # Cartesian coordinates (X, Y, Z)

    # Create a pyproj transformer
    transformer = pyproj.Transformer.from_crs(input_crs, output_crs, always_xy=True)

    # Convert geodetic coordinates to Cartesian coordinates
    x, y, z = transformer.transform(longitude, latitude, altitude)
    return x, y, z


# Convert to cartesian
x1, y1, z1 = geodetic_to_cartesian(lon0,lat0, alt0)
x0, y0, z0 = geodetic_to_cartesian(lon, lat, alt)

print(sqrt( (x0 - x1) ** 2) + (y0 - y1) ** 2 + (z0 - z1) ** 2)
