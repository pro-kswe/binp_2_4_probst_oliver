import random as rd

# Eingabe
zahlen = rd.sample(range(1, 1001), 20)

# Verarbeitung
summe = 0

for i in range(0, len(zahlen)):
    zahl = zahlen[i]
    summe = summe + zahl

# Ausgabe
print(zahlen)
print(f"Summe: {summe}")
