class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxStr = "";
        def expandCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1;
                right += 1;
            # exclusive of both left and right
            # after the loop, either left and right is out of bounds or s[left] != s[right]
            return s[left+1: right];
        for i in range(len(s)-1):
            odd = expandCenter(i, i)
            even = expandCenter(i, i+1)
            if len(odd) > len(maxStr):
                maxStr = odd
            if len(even) > len(maxStr):
                maxStr = even
        return maxStr





sol = Solution();
print(sol.longestPalindrome("cbbd"));
