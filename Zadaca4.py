# Regex se može iskoristiti za provjeru korisnikovog inputa;
# npr. ako tražimo od korisnika da odgovori "DA" ili "NE",
# a korisnik odgovori sa "Da, naravno" ili slično, pomoću
# regexa možemo provjeriti sadrži li poruka potrebnu ključnu riječ.
# Slično tako, možemo provjeravati inpute poput lozinki
# (određeni broj znakova),broja mobitela (određeni niz brojeva,
# zatim crtica ili razmak...), emaila (znak "@" i točka)...

# Zadatak:
# Potrebno napisati regex koji vraca podudaranje
# ukoliko se unese string koji počinje kao prvo
# slovo vašeg imena, a završava kao prvo slovo prezimena.
# String mora sadržavati bar jedan broj između 0 i 5 i razmak.

import re

firstName = input("Unesite ime: ")
lastName = input("Unesite prezime: ")
string = input("Unesite string za provjeru: ")

pattern = r"(?=.*\s)(?=.*[0-5])^{}.*{}$".format(re.escape(firstName[0]), re.escape(lastName[0]))
match = re.search(pattern, string, re.I)

if match:
    print("Podudaranje!")
else:
    print("Nema podudaranja!")
