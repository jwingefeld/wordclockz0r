import sys
import os	# for os.path.isfile
import time	# To obtain timestamps
import datetime
from subprocess import call	# To call OpenSCAD

piecesX = 8
piecesY = 8

def pad(n, digits=4):
	r = str(n)
	while (len(r) < digits):
		r = '0' + r
	return r

def generate_single(x, y):
	global piecesX, piecesY
	fileSCAD = 'puzzle004.scad'
	#CMD_OPENSCAD = 'lib/openscad/openscad'
	CMD_OPENSCAD = 'Z:/apps/_gfx/OpenSCAD/openscad.exe'
	fileOut = 'STLs/MaMu2013Puzzle004_' + str(piecesX) + 'x' + str(piecesY) + '_' + pad(x) + '-' + pad(y) + '.stl'
	cmd = CMD_OPENSCAD + ' -DpiecesX=' + str(piecesX) + ' -DpiecesY=' + str(piecesY) + ' -DrenderX=' + str(x) + ' -DrenderY=' + str(y) + ' -DPREVIEW=false -o ' + fileOut + ' ' + fileSCAD
	#cmd = CMD_OPENSCAD + ' -DpiecesX=' + str(piecesX) + ' -DpiecesY=' + str(piecesY) + ' -DrenderX=' + str(x) + ' -DrenderY=' + str(y) + ' -DPREVIEW=true -o ' + fileOut + ' ' + fileSCAD
	print('Calling "' + cmd + '"...')
	call(cmd)


#generate_single(2, 7)


# Generate all!
for y in xrange(piecesY):
	for x in xrange(piecesX):
		generate_single(x, y)


print("Done!")