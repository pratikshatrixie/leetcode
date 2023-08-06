def find_unique_number(arr_list):
    unique_number = 0
    for num in arr_list:
        unique_number ^= num
    return unique_number

arr_list = [2, 3, 1, 2, 3]
unique_number = find_unique_number(arr_list)
print("Unique number:", unique_number)