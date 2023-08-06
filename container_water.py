arr = [1,1]
multiply = 0
output = 0

for i in range(len(arr)):
    multiply = 0
    for j in range(i+1,len(arr)):
        if arr[i] <= arr[j]:
            multiply = arr[i]*(j-i)
        else:
            multiply = arr[j]*(j-i)
        
        output = max(output,multiply)

print(output)