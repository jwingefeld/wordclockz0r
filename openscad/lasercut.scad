string = "ESOISTPFÜNFZEHNZWANZIGDREIVIERTELUWOCHENENDEVORNACHTAGLHALBRELFÜNFZWEISIEBENICAZEHNEUNIEVIEREDREINSSECHSELACHTZWÖLFERKUHR"; // wordclock 
font = "techno overload (BRK)"; // font; kann der Font genau in der mitte gecentert werden?
frameSize = 250; // noch berücksichtigen!
columns = sqrt(len(string))-1; // Anzahl Reihen 
rows = sqrt(len(string))-1; // Anzahl Zeilen
font_size = 10; // muss irgendwann aus anderen Parametern generiert werden 
border = 5; // irgendwas um zu definieren wieviel platz alles hat
module lettermap (columns = columns, rows = rows, font_size = font_size, string = string, font = font) {
    for (i = [0:columns]) {
        for (j = [0:rows]) {
            translate ([j*font_size*2,-i*font_size*2,0]) text(string[i*11+j], font = font, size = font_size, halign = "center", valign = "center");
//            echo (i*11+j);
//            echo (string[i*11+j]);
        }
    }
}

difference () {
    square ((rows+1)*font_size*2); 
    translate ([font_size,(rows+1)*font_size*2-font_size,0]) lettermap();
}
/*
color ("black") translate ([0,-5,0]) difference () {
    translate ([0,-(rows+1)*font_size*2,0]) square ((rows+1)*font_size*2); 
    translate ([font_size,-font_size,0]) lettermap(font = "Crimescene Afterimage");
    }


NOTIZEN
- meine inputs : string von Paul, Fontauswahl, Rahmengröße und LEDstreifentyp von Jans webinterface,
- daraus generiere ich:
        ! irgendwie muss ich LEDstreifentyp berücksichtigen! 
        + fontsize irgendwie aus der Größe, Stringlänge und LEDstreifentyp
        + Aussenrand = Rahmengröße mit Ledstreifenabstand
        (+ Buchstabenabstand irgendwie aus der Größe und String_länge)
- Größe von IKEA-Bilderrahmengrößen raussuchen, und LEDstreifenspacing anschauen
- Dann e
 TODO:
    1 Größe in mm einbauen und daraus generieren
    2 Font-size aus Größe und Stringlänge
    3 LED-Typ einbauen, in Font-size berücksichtigen
    4 Jetzt brauchen wir nen definierten Aussenrand, aus Fontsize und Größe generieren
    4 rausfinden wie sich text(Size) in Y Richtung auswirkt, irgendwie muss ein Rand generiert werden, und es gibt fonts die superbreit sind z.B. Crimeszene. Brauch ich nen Korrekturfaktor?
    5 Irgendwie muss ich den LEDstreifentyp berücksichtigen!
