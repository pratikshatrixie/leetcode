class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        flag = 1
        max1 = 0
        min1 = 10000000000

        if len(nums) == 0:
            return 0
        if len(nums) == 1 and 1 in nums:
            return 0

        for i in nums:
            max1 = max(max1,i)
            min1 = min(min1,i)


        for i in range(min1,max1+1):
            if i not in nums:
                flag = 0
                return i
                break
            else:
                flag = 1
        
        if flag == 1 and 0 not in nums:
            return 0
            
        if flag == 1:
            return i+1