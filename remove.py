nums = [2, 3, 3, 2]
key = 3

# Iterate over a copy of the list
for num in nums[:]:
    if num == key:
        nums.remove(num)

print(nums)
