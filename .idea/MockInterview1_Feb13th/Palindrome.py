class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        beg = 0
        end = len(x)-1;
        while beg < end:
            if x[beg] != x[end]:
                return False;
            beg += 1;
            end -= 1;
        return True