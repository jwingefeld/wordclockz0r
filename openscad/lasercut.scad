string = "ESOISTPFÜNFZEHNZWANZIGDREIVIERTELUWOCHENENDEVORNACHTAGLHALBRELFÜNFZWEISIEBENICAZEHNEUNIEVIEREDREINSSECHSELACHTZWÖLFERKUHR"; // wordclock
led_spacing = 33.3/2; 
font = "Stockstill Solid"; //"techno overload (BRK)"; // "Crimescene Afterimage";//font; kann der Font genau in der mitte gecentert werden?
frameSize = 230; // standard Ikea frame, andere wäre 500, oder 320
3D = false; // z.B. für fräse
height = 4; // auch für 3D
columns = sqrt(len(string))-1; // Anzahl Reihen 
rows = sqrt(len(string))-1; // Anzahl Zeilen
font_size = led_spacing/2; // ich hab einfach mal angenommen, das font_size x2 ausreichend platz zwischen den Buchstaben lässt. Könnte bei bestimmten Fonts zu Problemen führen
inner_square = (rows+1)*font_size*2;
border = (frameSize - inner_square)/2;

module lettermap (columns = columns, rows = rows, font_size = font_size, string = string, font = font) { // muss bei nicht quadratischen layouts deutlich verändert werden
    for (i = [0:columns]) {
        for (j = [0:rows]) {
            translate ([j*font_size*2,-i*font_size*2,0]) text(string[i*(columns+1)+j], font = font, size = font_size, halign = "center", valign = "center");
        }
    }
}

module faceplate (frameSize = frameSize, border = border, font_size = font_size) {
    difference () {
        square (frameSize); 
        translate ([border+font_size,frameSize-border-font_size,0]) lettermap();
    }
}




if (3D == true) linear_extrude(height=height) faceplate();
else faceplate();

