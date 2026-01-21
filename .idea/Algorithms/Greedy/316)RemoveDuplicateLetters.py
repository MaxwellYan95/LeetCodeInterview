class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        minLetter = s;
        result = minLetter + "";
        for char in s[1:]:
            if char < minLetter:
                result = "" + char;
                minLetter = char;
            elif char not in result:
                result += "" + char;
        return result;
sol = Solution()
print(sol.removeDuplicateLetters("abd"))