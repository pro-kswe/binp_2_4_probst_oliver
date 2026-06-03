# Selection Sort
import random

# Eingabe
zahlen = random.sample(range(0, 71), 20)
print(zahlen)

# Verarbeitung
sortiert = []  # leere Liste
for _ in range(len(zahlen)): # len(zahlen) zählt wie viele Zahlen in der Liste sind, len steht für length
    kleinste_zahl = min(zahlen)
    sortiert.append(kleinste_zahl)  # Fügt das Minimum ans Ende der Liste hinzu
    zahlen.remove(kleinste_zahl)  # Löscht das Minimum aus der Liste

# Ausgabe
print(sortiert)
