from countries import countries
import random
import re

finalists = []

finalistNumbers = random.sample(range(len(countries)), 26)

for i in finalistNumbers:
    country = countries[i]

    finalists.append({"drzava": country[0], "izvodjac": country[1], "pjesma": country[2]})

for finalist in finalists:
    finalist["bodovi"] = 0

for i in range(len(countries)):
    vote = None
    while vote == i or vote == None:         
        vote = random.randint(0, len(finalistNumbers)-1)
        
    country = finalists[vote]
    country["bodovi"] += random.randint(1, 12)
    
    vote = None

# Privremeno
winner = finalists[0]
totalPoints = 0

for finalist in finalists[1:]:
    totalPoints += finalist["bodovi"]
    print(finalist)
    if finalist["bodovi"] > winner["bodovi"]:
        winner = finalist

print("---------------------------------------------------------------------------------------------------")
print("Pobjednik:")
print(winner)
print("Ukupno bodova:", totalPoints)
print("---------------------------------------------------------------------------------------------------")

print("Više od 10 slova u pjesmi:")
for finalist in finalists:
    if re.search(".{10,}", finalist["pjesma"]):
        print(finalist)

def DictToStr(dictionary):
    string = ""
    for key, value in dictionary.items():
        string += str(value) + ", "
    string = string.strip(", ")
    return string

file = open("Finalisti.txt", "w", encoding="utf-8")

for finalist in finalists:
    file.write(DictToStr(finalist) + "\n")
file.write("---------------------------------------------------------------------------------------------------\n")
file.write("Pobjednik:\n")
file.write(DictToStr(winner))

file.close()
