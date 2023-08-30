class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        output = -inf
        for i in range(len(nums)):
            output = max(output,nums[i])


        return nums.index(output)