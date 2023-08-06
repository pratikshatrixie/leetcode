arr = [-1,0]
output = -1
arr1 = []
flag = 0

for i in range(0,5):
    for j in range(i+1,5):
        if arr[i]+arr[j] == output:
            arr1.append(i+1)
            arr1.append(j+1)
            flag = 1
            break
    if flag == 1:
        break
    
print(arr1)