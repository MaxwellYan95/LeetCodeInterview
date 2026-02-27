class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True;
        elif len(t) == 0 and len(s) > 0:
            return False;
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])

sol = Solution()
print(sol.isSubsequence("abc", "asdfabsadgc"))