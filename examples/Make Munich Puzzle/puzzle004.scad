/*
*
* MakeMunich2013 Puzzle
*
*
* 2013-04-5 by Bernhard Slawik
* http://www.bernhardslawik.de, http://www.objektdruckerei.de
*
*/
use <makeMunichLogo.inc.scad>

// General configuration
EPS = 0.1;		// Eps(ilon) for floating point inprecisions
PREVIEW = true;	// Preview shows the borders and reduces quality
FN = (PREVIEW ? 8 : 32);	// Quality of round edges

// Size configuration
w = 500.0;		// Width of whole puzzle in millimeters
h = 500.0;		// Height of whole puzzle in millimeters
thick = 30.0;	// Thickness of one piece
baseThick = 10.0;	// Height/thickness of base
slantThick = 10.0;
space = 0.5;		// Spacing ON EACH EDGE

logoScale = h/120.0;	// Depends on how big the logo has been created


// Puzzle configuration
piecesX = 8;
piecesY = 8;

// Which part to render?
renderX = 1;
renderY = 0;


pieceW = w/piecesX;
pieceH = h/piecesY;

echo(str("Pieces are ", pieceW, " x ", pieceH, " mm each"));
if (PREVIEW) {
	echo("CAUTION!! You are currently rendering in PREVIEW (Draft) quality! Set variable 'PREVIEW' to false to generate high-res printable model!");
}

conBits = 3;
conDiam = min(pieceW, pieceH) / (conBits*2+1);
conSpace = min(pieceW, pieceH) / (conBits+1);
conNeck = conDiam;
conNeckDiam = conDiam/2;


// Implementation

function testBit_internal(rest, bit, i) =
	(i < 0) ? false :
	(rest >= pow(2, i)) ? (
		(i == bit) ? true :
		testBit_internal(rest - pow(2, i), bit, i-1)
	) :
		(i == bit) ? false :
		testBit_internal(rest, bit, i-1)
	;

// Check if the given bit is set in given code
function testBit(code, bit) =
	testBit_internal(code, bit, conBits-1);


module connector(code, kind=0, extra=0, extraT=0) {
	if (code >= 0)
	for (i=[0:conBits-1])
		translate([conSpace + i*conSpace, 0, 0]) {

			// EVERY thing has a connector
			translate([-conNeckDiam/2 - extra, -(EPS + space), -extraT])
			cube([conNeckDiam + 2*extra, EPS + conNeck + space + extra, thick + 2*extraT]);

			if (testBit(code, i)) {
				translate([0, conNeck, -extraT])
				if (kind == 0)
					rotate([0, 0, 180/8])
					cylinder(r=conDiam/2 + extra, h=thick+2*extraT, $fn=8);
				else
					rotate([0, 0, 180+90/3])
					cylinder(r=conDiam/2 + extra, h=thick+2*extraT, $fn=3);
			}
		}
}


// Draw one puzzle piece base shape
module piece(codeUp=0, codeDown=0, codeLeft=0, codeRight=0, space=space) {
	difference() {
		union() {
			translate([space, space, 0])
			cube([pieceW - space*2, pieceH - space*2, thick]);
	
			translate([pieceW*0, pieceH])
			connector(codeUp, kind=0, extra=-space);
	
			translate([pieceW, pieceH])
			rotate([0,0,-90])
			connector(codeRight, kind=1, extra=-space);
		}

		union() {
			translate([pieceW*0, pieceH*0])
			connector(codeDown, kind=0, extra=space, extraT=EPS);
	
			translate([pieceW*0, pieceH])
			rotate([0,0,-90])
			connector(codeLeft, kind=1, extra=space, extraT=EPS);
		}
	}
/*
	translate([pieceW, pieceH])
	rotate([0,0,-90])
	connector(code);
*/
}

// Draw all puzzle pieces' base shapes (use it for intersecting a 3D model)

module piece_single(x, y) {
	translate([-w/2, -h/2, 0])
	translate([x*pieceW, y*pieceH, 0])
	piece(
		codeUp = (y >= piecesY-1 ? -1 : y+1),
		codeDown = (y <= 0 ? -1 : y),
		codeLeft = (x <= 0 ? -1 : x),
		codeRight = (x >= piecesX-1 ? -1 : x+1),
		space=space
	);
}

module pieces() {
	for(y=[0:piecesY-1])
	for(x=[0:piecesX-1])
	piece_single(x, y);
}


// Draw the logo in 3D
module logo() {

	if (PREVIEW) {
		* //Disabled
		// Show bounds
		%translate([-w/2, -h/2, 0])
		cube([w, h, thick]);
	}


	// Base
	translate([-w/2, -h/2, 0])
	cube([w, h, baseThick]);



	// Add some nice bevel
	hull() {
		translate([-w/2, -h/2, baseThick])
		cube([w, h, EPS]);

		translate([0, 0, baseThick + slantThick/2])
		linear_extrude(height=EPS)
		scale(logoScale)
		mmLogo(preview=PREVIEW);
	}


	// Extrude logo
	translate([0, 0, EPS])
	linear_extrude(height=thick-EPS)
	scale(logoScale)
	mmLogo(preview=PREVIEW);
}


// Combine logo and pieces to create 3D puzzle pieces
//logo();
//piece(1*1 + 0*2 + 1*4 + 0*8 + 1*16 + 0*32 + 1*64 + 0*128);
//pieces();


// Render one piece
echo(str("Rendering puzzle piece x=", renderX, "/", piecesX, ", y=", renderY, "/", piecesY, " ..."));


if ((renderX >= 0) && (renderX < piecesX) && (renderY >= 0) && (renderY < piecesY)) {
	intersection() {
		logo();
	
		piece_single(x=renderX, y=renderY);
	}
} else {
	echo("The given coordinates are out of range!");
}
