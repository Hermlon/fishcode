Fragen:
    -Bewegung immer in Drehrichtung?
    -Eine Bewegungs- und eine Schussrichtung?
    -Geschwindigkeit durch Steuerungsscript steuerbar (stufenlos? oder normal und sprinten?)
    -Geschwindigkeit ausschließlich von Energie abhängig (Je mehr Energie desto langsamer)[Würde ich bevorzugen]

Features:
    -Steuerungsscript kann Pixel der Spielfigur selbst setzen, (transparenter Hintergrund)

Score System:
    -Energie:
        -wird getroffen: Energie --
        -trifft: Energie ++
    
Plan:
    -Client bekommt über Server alle Informationen über verfügbare Karten, Leaderboard, die Karte mit den enthaltenen Spieler, zeigt diese an, hochladen von neuen Steuerungsscripten
    -Server berechnet Position, Aktionen der Spieler, deren Bewegung wird von deren Steuerungsscripten bestimmt, welche vom Server mit aktuellen parametern ausgeführt werden
