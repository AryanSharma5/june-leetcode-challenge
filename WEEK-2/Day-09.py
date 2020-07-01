class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        j = 0
        for i in range(len(s)):
            while j < len(t) and s[i] != t[j]:
                j += 1
            if j>=len(t):
                return False
            count += 1
            j += 1
        if count == len(s):return True
        else:return False
        