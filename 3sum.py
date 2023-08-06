arr = [0,0,1]
output = set()
flag = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                output.add(triplet)
            else:
                flag = 1

output_list = [list(triplet) for triplet in output]

if flag == 1:
    print("no combination")

else:
    print(output_list)