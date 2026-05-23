# Eingabe
k = int(input("Nach welcher Zahl möchten Sie suchen?"))
zahlen = [71, 26, 8, 42, 90, 5, 7, 20, 3, 99, 1023, 50]


# Verarbeitung
resultat = "NEIN"

for i in range(0, len(zahlen)):
    
    zahl = zahlen[i]
    
    if zahl == k:
        
        resultat = "JA"


# Ausgabe
print(f"Befindet sich {k} in der Liste? {resultat}")
