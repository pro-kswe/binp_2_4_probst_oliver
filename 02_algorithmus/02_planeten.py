import random as rd

planeten = ["Merkur", "Venus", "Erde", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
print(planeten)
print(planeten[0])
print(planeten[1])
print(planeten[2])
print(planeten[3])
print(planeten[4])
print(planeten[5])
print(planeten[6])
print(planeten[7])

for _ in range(5):
    print("Zufälliger Planet")
    i = rd.randrange(0, 8)
    print(planeten[i])
    