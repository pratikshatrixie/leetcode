list1 = [999]
list2 = [111]
list3 = []
list4 = []
i = 0
j = 0
output = 0

list5 = str(list1)
list6 = str(list2)

while i!=len(list5) and j!=len(list6):
    a = list5[i].split()
    b = list6[j].split()
    
    y = 0
    z = 0
    while y!=len(a) and z!=len(b):
        if (a[y] == "[" or a[y] == "]" or a[y] == "," or a[y] == "'") or (b[z] == "[" or b[z] == "]" or  b[z] == "," or  b[z] == "'"):
            y += 1
            z += 1
            continue
        else:
            if int(a[y]) >= int(b[z]):
                output = output + (int(a[y])-int(b[z]))
            else:
                output = output + (int(b[z])-int(a[y]))
        y += 1
        z += 1
        
    i += 1
    j += 1
            
print(output)
