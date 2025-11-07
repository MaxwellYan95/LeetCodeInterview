class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = self.changeFormat(s)
        p1 = 0;
        p2 = len(newS)-1;
        while p1 < p2 and p1 < len(newS) and p2 >= 0:
            if newS[p1] != newS[p2]:
                return False;
            p1 = p1 + 1;
            p2 = p2 - 1;
        return True;

    def changeFormat(self, s: str) -> str:
        result = ""
        for letter in s:
            if letter.isalnum():
                result += letter;
        return result.lower();

sol = Solution();
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome(".,"))
print(sol.isPalindrome(".,"))

