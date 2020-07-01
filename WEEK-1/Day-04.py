class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s)%2==0:
            i = 0
            j = len(s) - 1
            while i<j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        else:
            i = 0
            j = len(s) - 1
            while i!=j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return s