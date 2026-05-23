import random as rd

# Eingabe
zahlen = rd.sample(range(1, 1001), 20)

# Verarbeitung
maximum = zahlen[0]

for i in range(1, len(zahlen)):
    zahl = zahlen[i]
    if zahl > maximum:
        maximum = zahl

# Ausgabe
print(zahlen)
print(f"Grösste Zahl: {maximum}")
