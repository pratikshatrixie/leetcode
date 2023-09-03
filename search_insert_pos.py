class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i

        if target not in nums:
            return (len(nums))
             