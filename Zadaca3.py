from random import randint
from random import uniform

firstNames = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
lastNames = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

workers = []
workersAndPay = []
total = 0

print("Radnici:\n")
while len(workers)<15:
    worker  = {}
    worker["Ime"] = firstNames[randint(0, len(firstNames)-1)]
    worker["Prezime"] = lastNames[randint(0, len(lastNames)-1)]
    worker["Satnica"] = round(uniform(4, 6), 2)
    workers.append(worker)
    print(worker)

print("\n-------------------------------------------------------------------------------\n")

print("Radnici s tjednim satima:\n")
for worker in workers:
    worker["Tjedni sati"] = randint(20, 30)
    print(worker)

    pay = round(worker["Satnica"] * worker["Tjedni sati"], 2)
    total += pay
    
    workersAndPay.append((worker["Ime"], worker["Prezime"], pay))

print("\n-------------------------------------------------------------------------------\n")

print("Radnici i isplata:\n")
for worker in workersAndPay:
    print(worker)

print("\n-------------------------------------------------------------------------------\n")

averagePay = round(total/len(workersAndPay), 2)
print("Ukupna isplata:", round(total, 2))
print("Prosječna isplata:", averagePay)

print("\n-------------------------------------------------------------------------------\n")

print("Iznad prosječnu plaću imaju:")
for worker in workersAndPay:
    if worker[2] > averagePay:
        print(worker)
