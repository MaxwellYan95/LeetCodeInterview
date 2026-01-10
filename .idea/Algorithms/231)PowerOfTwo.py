class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True;
        p = 2;
        while p < n:
            p = p * 2;
        return p == n;