arr = [3,4,5,6]
sum = 9
list1 = []
list2 = []

for i in range(4):
    for j in range(i+1,4):
        if arr[i] + arr[j] == sum:
            list1.append(arr[i])
            list2.append(arr[j])

print(list1)
print(list2)