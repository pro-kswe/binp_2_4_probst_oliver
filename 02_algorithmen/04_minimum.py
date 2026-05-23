import random as rd

# Eingabe
zahlen = rd.sample(range(1, 1001), 20)

# Verarbeitung
minimum = zahlen[0]

for i in range(1, len(zahlen)):
    zahl = zahlen[i]
    if zahl < minimum:
        minimum = zahl

# Ausgabe
print(zahlen)
print(f"Kleinste Zahl: {minimum}")
