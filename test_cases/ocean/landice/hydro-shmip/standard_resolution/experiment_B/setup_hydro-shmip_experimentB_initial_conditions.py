#!/usr/bin/env python
'''
Generate initial conditions for hydro-SHMIP land ice test case B
Details here: http://shmip.bitbucket.org/
'''

from netCDF4 import Dataset as NetCDFFile
import numpy as np
import sys
import shutil

# Parse options
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", type='string', help="file to setup", metavar="FILE")
parser.add_option("-a", dest="afile", type='string', help="restart file from test A1 to use to set up this test", metavar="FILE")
parser.add_option("-n", "--number", dest="number", type='int', help="test variant to set up, 1-5", metavar="NUMBER")
options, args = parser.parse_args()
if not options.filename:
   options.filename = 'landice_grid.nc'
   print 'No file specified.  Attempting to use landice_grid.nc'

if not options.afile:
   sys.exit("Error: A restart file from test A1 is required to set up this test.  Specify with -a")

# copy the restart file to be the new input file
shutil.copyfile(options.afile, options.filename)

# Open the file, get needed dimensions
gridfile = NetCDFFile(options.filename,'r+')

b_moulin = {}  # empty dictionary

b_moulin[1]=((0,59000,8000,90.0),)


b_moulin[2]= ((0,30000,3000,9.0),
                (1,8000,4000,9.0),
                (2,60000,7000,9.0),
                (3,35000,9000,9.0),
                (4,46000,10000,9.0),
                (5,26000,11000,9.0),
                (6,7000,12000,9.0),
                (7,5000,14000,9.0),
                (8,9000,14000,9.0),
                (9,39000,16000,9.0),
                )

b_moulin[3] = (
(0,35000,2000,4.5),
(1,5000,3000,4.5),
(2,84000,3000,4.5),
(3,97000,3000,4.5),
(4,10000,5000,4.5),
(5,5000,6000,4.5),
(6,44000,9000,4.5),
(7,47000,9000,4.5),
(8,20000,10000,4.5),
(9,33000,11000,4.5),
(10,19000,12000,4.5),
(11,33000,14000,4.5),
(12,75000,14000,4.5),
(13,13000,15000,4.5),
(14,37000,15000,4.5),
(15,5000,16000,4.5),
(16,12000,16000,4.5),
(17,5000,17000,4.5),
(18,67000,17000,4.5),
(19,69000,18000,4.5),
                )

b_moulin[4] = (
(0,14000,1000,1.8),
(1,26000,1000,1.8),
(2,82000,1000,1.8),
(3,23000,2000,1.8),
(4,55000,2000,1.8),
(5,73000,2000,1.8),
(6,98000,2000,1.8),
(7,36000,3000,1.8),
(8,23000,4000,1.8),
(9,62000,4000,1.8),
(10,10000,5000,1.8),
(11,29000,5000,1.8),
(12,51000,5000,1.8),
(13,88000,5000,1.8),
(14,9000,6000,1.8),
(15,23000,6000,1.8),
(16,63000,6000,1.8),
(17,79000,6000,1.8),
(18,82000,6000,1.8),
(19,5000,7000,1.8),
(20,6000,7000,1.8),
(21,8000,7000,1.8),
(22,10000,7000,1.8),
(23,34000,8000,1.8),
(24,12000,9000,1.8),
(25,8000,10000,1.8),
(26,12000,10000,1.8),
(27,22000,10000,1.8),
(28,93000,10000,1.8),
(29,20000,11000,1.8),
(30,74000,11000,1.8),
(31,6000,12000,1.8),
(32,22000,12000,1.8),
(33,64000,12000,1.8),
(34,65000,12000,1.8),
(35,5000,13000,1.8),
(36,8000,13000,1.8),
(37,15000,13000,1.8),
(38,52000,13000,1.8),
(39,5000,14000,1.8),
(40,6000,14000,1.8),
(41,11000,14000,1.8),
(42,80000,14000,1.8),
(43,12000,15000,1.8),
(44,88000,15000,1.8),
(45,16000,16000,1.8),
(46,5000,18000,1.8),
(47,12000,18000,1.8),
(48,57000,18000,1.8),
(49,86000,18000,1.8),
                )

b_moulin[5] = (
(0,5000,1000,0.9),
(1,8000,1000,0.9),
(2,27000,1000,0.9),
(3,44000,1000,0.9),
(4,75000,1000,0.9),
(5,78000,1000,0.9),
(6,94000,1000,0.9),
(7,11000,2000,0.9),
(8,29000,2000,0.9),
(9,43000,2000,0.9),
(10,56000,2000,0.9),
(11,65000,2000,0.9),
(12,68000,2000,0.9),
(13,77000,2000,0.9),
(14,6000,3000,0.9),
(15,90000,3000,0.9),
(16,99000,3000,0.9),
(17,6000,4000,0.9),
(18,8000,4000,0.9),
(19,12000,4000,0.9),
(20,21000,4000,0.9),
(21,50000,4000,0.9),
(22,56000,4000,0.9),
(23,67000,4000,0.9),
(24,89000,4000,0.9),
(25,6000,5000,0.9),
(26,13000,5000,0.9),
(27,14000,5000,0.9),
(28,23000,5000,0.9),
(29,32000,5000,0.9),
(30,40000,5000,0.9),
(31,52000,5000,0.9),
(32,5000,6000,0.9),
(33,19000,6000,0.9),
(34,31000,6000,0.9),
(35,32000,6000,0.9),
(36,64000,6000,0.9),
(37,57000,7000,0.9),
(38,66000,7000,0.9),
(39,94000,7000,0.9),
(40,5000,8000,0.9),
(41,41000,8000,0.9),
(42,5000,9000,0.9),
(43,6000,9000,0.9),
(44,8000,9000,0.9),
(45,20000,9000,0.9),
(46,22000,9000,0.9),
(47,28000,9000,0.9),
(48,61000,9000,0.9),
(49,64000,9000,0.9),
(50,71000,9000,0.9),
(51,5000,10000,0.9),
(52,12000,10000,0.9),
(53,15000,10000,0.9),
(54,20000,10000,0.9),
(55,30000,10000,0.9),
(56,73000,10000,0.9),
(57,88000,10000,0.9),
(58,5000,11000,0.9),
(59,8000,11000,0.9),
(60,47000,11000,0.9),
(61,79000,11000,0.9),
(62,14000,12000,0.9),
(63,17000,12000,0.9),
(64,31000,12000,0.9),
(65,91000,12000,0.9),
(66,5000,13000,0.9),
(67,7000,13000,0.9),
(68,10000,13000,0.9),
(69,15000,13000,0.9),
(70,34000,13000,0.9),
(71,41000,13000,0.9),
(72,49000,13000,0.9),
(73,54000,13000,0.9),
(74,5000,14000,0.9),
(75,11000,14000,0.9),
(76,13000,14000,0.9),
(77,37000,14000,0.9),
(78,58000,14000,0.9),
(79,5000,15000,0.9),
(80,13000,15000,0.9),
(81,14000,15000,0.9),
(82,17000,15000,0.9),
(83,23000,16000,0.9),
(84,30000,16000,0.9),
(85,38000,16000,0.9),
(86,39000,16000,0.9),
(87,55000,16000,0.9),
(88,57000,16000,0.9),
(89,5000,17000,0.9),
(90,13000,17000,0.9),
(91,22000,17000,0.9),
(92,54000,17000,0.9),
(93,83000,17000,0.9),
(94,5000,18000,0.9),
(95,12000,18000,0.9),
(96,47000,18000,0.9),
(97,53000,18000,0.9),
(98,74000,18000,0.9),
(99,94000,18000,0.9),
)
# modify melt inputs - basalMeltInput remains the same as A1
moulin = gridfile.variables['externalWaterInput'][0,:]
gridfile.variables['basalMeltInput'][0,:] = 7.93e-11 * 1000.0  # Put background input here
xCell = gridfile.variables['xCell'][:]
yCell = gridfile.variables['yCell'][:]
areaCell= gridfile.variables['areaCell'][:]

moulin[:] = 0.0
for m in b_moulin[options.number]:
    n = m[0]
    x = m[1]
    y = m[2]
    Q = m[3]
    # Find cell for this location
    dist = ((x-xCell)**2 + (y-yCell)**2)**0.5
    ind = np.argmin(dist)
    print 'Moulin {}: x={}, y={}; xCell={}; yCell={}       dist={}'.format(n, x, y, xCell[ind], yCell[ind], dist[ind])
    moulin[ind] = moulin[ind] + Q * 1000.0 / areaCell[ind]  # convert from m3/s to kg/m2/s


gridfile.variables['externalWaterInput'][0,:] = moulin
gridfile.close()

print 'Successfully added initial conditions to: ', options.filename

