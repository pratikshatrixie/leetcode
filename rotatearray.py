arr = [7,8,2,3,4,1]
k = 2
size = len(arr)
arr1 = [0,0,0,0,0,0]

for i in range(size):
    if i+k <= size-1:
        arr1[i+k] = arr[i]

        
    else:
        difference = (i+k)-(size)
        arr1[difference] = arr[i]

        
print(arr1)