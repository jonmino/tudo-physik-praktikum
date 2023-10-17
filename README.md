# tudo-physik-praktikum

Dieses Repository bietet eine Grundlage für das Praktikum der Fakultät Physik an der TU Dortmund.
Es enthält ein Template/Beispiel (`vXXX`) wie ein solches Protokoll erstellt werden kann, eine Liste an nützlichen Programmen, welche als Conda Environment installiert werden können (`prak.yml`). Außerdem werden diverse Altprotokolle bereitgestellt.
Alle in den Protokollen verlinkten Quellen sind in `programme.bib` und `lit.bit` zu finden.
Die globale Makefile bietet folgende Befehle:

- `make vXXX` -> Versuch XXX bauen
- `make cXXX` -> build Verzeichnis von Versuch XXX löschen
- `make all` -> Alle Versuche bauen
- `make clean` -> Alle build Ordner löschen

## Empfehlungen

- Es lohnt sich etwas Zeit zu investieren um die MAKEFILES zu verstehen, wie diese interagieren und welchen Zweck diese erfüllen, da diese dann auf jeden Versuch zugeschnitten werden können.
- Die Objektorientierte Variante mit Matplotlib Plots zu erstellen mag zwar anfangs etwas komplizierter sein. bietet dafür aber mehr Möglichkeiten -> https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces
- Generell sind die meisten Probleme mittels Numpy über Matrixoperationen lösbar, welche die Laufzeit deutlich verbessern. Schleifen (For,While) sollten möglichst vermieden werden, da Python verglichen mit dem in C(++) implementierten Numpy recht langsam ist.
- Plots sollten wenn möglich so erstellt werden, dass sie auch für Farbenblinde beziehungsweise als Grayscale-Druck lesbar sind -> https://matplotlib.org/stable/users/explain/colors/colormaps.html
