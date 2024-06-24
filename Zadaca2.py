#Modificirati po potrebi

csvFilePath = "./Zadaca2.csv"
RowNumbersToDiscardFromTop = 4
RowNumbersToDiscardFromBottom = 60

#################################################################

i=0
students=[]
marks={}

def Grading(points):
    if points < 50:
        return "Nedovoljan - 1"
    elif points >= 50 and points < 65:
        return "Dovoljan - 2"
    elif points >= 65 and points < 80:
        return "Dobar - 3"
    elif points >= 80 and points < 90:
        return "Vrlodobar - 4"
    else:
        return "Odličan - 5"

from csv import reader
with open(csvFilePath, encoding = "UTF-8") as readObj:
    csvReader = reader(readObj)
    for row in csvReader:

        i += 1
        if i <= RowNumbersToDiscardFromTop or i >= RowNumbersToDiscardFromBottom:
            continue
        
        student = (row[0], row[1], int(row[2]))
        students.append(student)

print("Položili:\n")
for student in students:
    if student[2] > 49:
        print(student)

print("\n---------------------------------------\n")

studentsSorted = sorted(students, key=lambda x:x[1])

print("Ocjene:\n")    
for name, lastName, points in studentsSorted:
    marks[name, lastName] = Grading(points)

for student, mark in marks.items():
    print(student, ":", mark)
