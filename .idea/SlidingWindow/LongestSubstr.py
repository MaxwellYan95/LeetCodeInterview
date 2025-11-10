class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sList = list(s)
        maxLen = 0;
        lower = 0;
        for upper in range(len(sList)):
            curS = s[upper];
            while curS in s[lower:upper]:
                lower += 1;
            maxLen = max(maxLen, upper-lower+1);
        return maxLen;

