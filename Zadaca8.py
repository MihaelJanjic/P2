def ReverseString(string):
    if len(string)<=1:
        return string
    
    return ReverseString(string[1:]) + string[0]

print(ReverseString("123456"))
