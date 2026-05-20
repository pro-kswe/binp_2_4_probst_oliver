import random as rd

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
index = rd.randrange(0, 7)
wochentag = wochentage[index]
print(f"Heute ist: {wochentag}")
if wochentag != "Sonntag":
    print("Heute ist ein Werktag.")
print("Ich wünsche Ihnen einen schönen Tag.")
