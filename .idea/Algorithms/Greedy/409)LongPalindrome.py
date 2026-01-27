class Solution:
    def longestPalindrome(self, s: str) -> int:
        oneLetter = 0;
        lst = sorted(list(s))
        index = 0;
        maxLen = 0;
        while index < len(lst):
            if index == len(lst)-1:
                oneLetter += 1;
                index += 1;
            elif lst[index] == lst[index+1]:
                maxLen += 2;
                index += 2;
            else:
                oneLetter += 1;
                index += 1;
        if oneLetter > 0:
            return maxLen + 1;
        return maxLen