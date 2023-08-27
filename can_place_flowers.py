class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num = len(flowerbed)
        i = 0
        output = 0

        while i < num:
            if i == num - 1:
                if flowerbed[i] == 0:
                    output += 1
                break
            elif flowerbed[i] == 1:
                i += 2
            else:
                if flowerbed[i+1] == 0:
                    output += 1
                    i += 2
                else:
                    i += 3

        return output >= n
