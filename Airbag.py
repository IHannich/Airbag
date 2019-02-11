import adxl355 as acelerometro

print(dir (acelerometro))

"""
Usage example for ADXL355 Python library
This example prints on console the current values
of axes on accelerometer
"""

import sys
sys.path.append('../lib/')

from adxl355 import ADXL355  # pylint: disable=wrong-import-position

device = ADXL355()           # pylint: disable=invalid-name
dimension = device.get_dimension()     # pylint: disable=invalid-name
print(dimension) 

while True:
    dimension = device.get.dimension()
    sleep(1)
    if dimension x >130°:
        gpio.output(led1,True)
    else:
        gpio.output(False)

#xdxdxd
