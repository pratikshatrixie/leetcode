from ast import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        x = -1
        output = []
        final = []

        if len(nums) == 0:
            output.append(x)
            output.append(x)
            return output

       
        flag = 0
        for i in range(len(nums)):
            if nums[i] == target:
                flag = 1
                output.append(i)
                y = i

        if flag == 0:
            output.append(x)
            output.append(x)
            return output

        if len(nums) == 1 and flag == 0:
            output.append(x)
            return output

        if len(nums) == 1:
            output.append(y)
            return output

        if len(output) == 1:
            output.append(y)
            return output
        
        if len(output) > 2:
            final.append(output[0])
            final.append(output[len(output)-1])
            return final

        return output

        
            