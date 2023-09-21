class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        flag = 0
        for i in nums:
            if i == 0:
                flag = 0
            else:
                flag = 1
                break
        if flag == 1:
            sorted_numbers = sorted(nums, key=lambda x: len(str(x)), reverse=True)

            numbers = sorted(nums, key=lambda x: str(x)*len(str(sorted_numbers[0])), reverse=True)

            final = ""
            for i in numbers:
                final += str(i)

            return final 
        else:
            return "0"              