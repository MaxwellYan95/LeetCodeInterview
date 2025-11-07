class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower();
        p1 = 0;
        p2 = len(lowerS)-1;
        while p1 < p2 and p1 < len(lowerS) and p2 >= 0:
            while p1 < len(lowerS)-1 and not lowerS[p1].isalpha():
                p1 = p1 + 1;
            while p2 >= 1 and not lowerS[p2].isalpha():
                p2 = p2 - 1;
            if lowerS[p1] != lowerS[p2] and lowerS[p1].isalpha() and lowerS[p2].isalpha():
                return False;
            p1 = p1 + 1;
            p2 = p2 - 1;
        return True;

sol = Solution();
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome(".,"))
