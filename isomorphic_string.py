class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_mapping = {}  # To store the mapping of characters
        
        for i in range(len(s)):
            if s[i] in char_mapping:
                if char_mapping[s[i]] != t[i]:
                    return False
            else:
                # Check if the character in t has already been mapped to
                if t[i] in char_mapping.values():
                    return False
                char_mapping[s[i]] = t[i]
        
        return True
