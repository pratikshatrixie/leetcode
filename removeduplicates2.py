arr = [1,1,1,1,2,3,3,3,3,3,3,4,4,4,4,4]

count = 0
add = 0
j = 0
flag = 0

for i in range(len(arr)):
    store = arr[j]
    i = j
    
    while (arr[i]==store):
        count += 1
        i += 1
        if (i == len(arr)):
            if count > 2:
                count = 2
            add += count
            flag = 1
            break
    
    if (flag == 1):
        break
        
    if count > 2:
        count = 2

    add += count
    j = i
    count = 0
    
print("add", add)