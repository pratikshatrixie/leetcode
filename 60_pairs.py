class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count_modulo = [0] * 60
        count = 0  # Initialize the count of pairs

        for duration in time:
            # Calculate the remainder when the duration is divided by 60
            remainder = duration % 60

            # Calculate the complement duration modulo 60 (the other part of the pair)
            complement = (60 - remainder) % 60

            # Increment the count by the number of songs with the complement duration
            count += count_modulo[complement]

            # Increment the count_modulo list for the current duration
            count_modulo[remainder] += 1

        return count

            