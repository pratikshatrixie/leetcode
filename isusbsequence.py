class Solution(object):
    def isSubsequence(self, s, t):
        output = []

        for i in t:
            if i in s:
                output.append(i)

        final = "".join(output)

        if (final == s):
            print("true")
        else:
            print("false")