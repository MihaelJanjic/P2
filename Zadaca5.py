import re

emailPattern = r"[a-z]{3,20}\.[a-z]{3,20}@fpmoz\.sum\.ba"
eduidPattern = r"[a-z]{4,21}[0-9]*@sum\.ba"

while True:
    email = input("Unesite e-mail: ")

    if re.search(emailPattern, email) == None:
        print("Nevažeći unos!")
    else:
        break
    
print("Uspješno uneseno!\n")

while True:
    eduid = input("Unesite eduid: ")

    if re.search(eduidPattern, eduid) == None:
        print("Nevažeći unos!")
    else:
        break

print("Uspješno uneseno!\n")

print("Svi podatci uspješno uneseni!")
