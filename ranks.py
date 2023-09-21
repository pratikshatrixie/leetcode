class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output = []
        sorted_numbers = sorted(score,reverse=True)

        for i in range(len(score)):
            if score[i] == sorted_numbers[0]:
                output.append("Gold Medal")
            elif score[i] == sorted_numbers[1]:
                output.append("Silver Medal")
            elif score[i] == sorted_numbers[2]:
                output.append("Bronze Medal")
            else:
                output.append(str(sorted_numbers.index(score[i])+1))

        return output