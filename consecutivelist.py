def longestConsecutive(nums):
    # Convert the input list to a set for faster lookup
    num_set = set(nums)

    # Variable to store the length of the longest consecutive sequence
    longest_streak = 0

    # Iterate through each number in the input list
    for num in nums:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Increment the current number until it is no longer in the set
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak if necessary
            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# Example usage:
nums = [100, 4, 200, 1, 3, 2, 5]
result = longestConsecutive(nums)
print(f"The longest consecutive sequence is {result}")
