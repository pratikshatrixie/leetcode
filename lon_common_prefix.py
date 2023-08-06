from ast import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        common_prefix = []
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for string in strs:
                if string[i] != char:
                    return "".join(common_prefix)
            common_prefix.append(char)

        return "".join(common_prefix)
