class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), 0, -1):
            for start in range(0, len(s)-length + 1):
                if self.check(s[start: start+length]) == True:
                    return s[start: start+length];
        return "";

    def check(self, s: str) -> bool:
        left = 0;
        right = len(s)-1;
        while left<right:
            if s[left] != s[right]:
                return False;
            left = left + 1;
            right = right - 1;
        return True;

sol = Solution();
print(sol.longestPalindrome("cbbd"));
