from random import randint

i=0

imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjene = []

popisOcjena = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for ime in imena:
    ocjene.append(randint(1,5))
    print(ime, "-", ocjene[i])
    i += 1
    
for ocjena in ocjene:
    popisOcjena[ocjena] += 1

print("\nPopis ocjena:")
print(popisOcjena, "\n")
print("postotak prolaznosti:")
print(str(round((popisOcjena[2] + popisOcjena[3] + popisOcjena[4] + popisOcjena[5]) / i * 100, 2)) +  str("%"))
