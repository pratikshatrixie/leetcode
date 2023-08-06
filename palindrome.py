strr = "A man, a plan, a canal: Panama       "
str2 = []
str3 = []
output = ""
output2 = ""
str1 = strr.casefold()

for i in str1:
    if i == ' ' or i == ',' or i == ':' or i == ';' or i == '.' or i == '!':
        continue
    else:
        str2.append(i)
    
n = len(str2) - 1

while(n>=0):
    str3.append(str2[n])
    n -= 1

output4 = output2.join(str2)
output1 = output.join(str3)

if output4 == output1:
    print("true")
else:
    print("false")