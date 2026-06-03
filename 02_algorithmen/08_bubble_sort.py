# Bubble Sort
import random

# Eingabe
zahlen = random.sample(range(0, 71), 20)
print(zahlen)

# Verarbeitung
while True:
    getauscht = "NEIN"
    for i in range(0, 19):
        zahl_1 = zahlen[i]
        zahl_2 = zahlen[i + 1]
        if zahl_2 < zahl_1:
            zahlen[i] = zahl_2
            zahlen[i + 1] = zahl_1
            getauscht = "JA"
    if getauscht == "NEIN":
        break

# Ausgabe
print(zahlen)
