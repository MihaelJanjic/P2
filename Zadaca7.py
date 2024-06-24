def Even(a):
    for i in range(a):
        if i%2 == 0 and i != 0:
            yield i

def Odd(a):
    for i in range(a):
        if i%2 == 1:
            yield i

value = int(input("Unesi neki broj: "))

odd = Odd(value)
even = Even(value)

print("\nNeparni:")
for i in odd:
    print(i)

print("\nParni:")
for i in even:
    print(i)
