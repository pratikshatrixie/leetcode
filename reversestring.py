str = input("Enter the string");
str2 = ""

s = len(str) - 1

while s>=0:
    str2 = str2 + str[s]
    s = s - 1
    
print(str2)