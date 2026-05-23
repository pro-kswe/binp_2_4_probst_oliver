import random as rd

# Eingabe
k = int(input("Nach welcher Zahl möchten Sie suchen?"))
zahlen = rd.sample(range(1, 1001), 20)


# Verarbeitung
resultat = "NEIN"

for i in range(0, len(zahlen)):
    
    zahl = zahlen[i]
    
    if zahl == k:
        
        resultat = "JA"


# Ausgabe
print(f"Befindet sich {k} in der Liste? {resultat}")
