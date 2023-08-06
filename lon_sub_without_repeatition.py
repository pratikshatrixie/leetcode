string = "pwwkew"
current = []
length = 0
output = 0

for i in range(0,len(string)):
    if string[i] not in current:
        current.insert(i,string[i])
        length += 1

    else:
        length = 1
    
    output = max(output,length)

print(output)
