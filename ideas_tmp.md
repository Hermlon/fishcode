Spieler:
  - bewegt und schießt in eine Rotationsrichtung
  - Geschwindigkeit: Je mehr Energie, desto langsamer
  - Spieler kennt jederzeit das gesamte Spielfeld

Features: / Ideen:
    -Steuerungsscript kann Pixel der Spielfigur selbst setzen, (transparenter Hintergrund)
    - (auch für Schüsse?) Ja, durch Texture theoretisch implementierbar

Score System:
    -Energie:
        -wird getroffen: Energie --
        -trifft: Energie ++

Plan:
    -Client bekommt über Server alle Informationen über verfügbare Karten, Leaderboard, die Karte mit den enthaltenen Spieler, zeigt diese an, hochladen von neuen Steuerungsscripten
    -Server berechnet Position, Aktionen der Spieler, deren Bewegung wird von deren Steuerungsscripten bestimmt, welche vom Server mit aktuellen parametern ausgeführt werden

Issues:
  - import funktioniert noch nicht
  - noch nicht getestet
