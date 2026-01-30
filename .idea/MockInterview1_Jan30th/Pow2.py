class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        curN = n;
        while curN != 1:
            if curN % 2 != 0:
                return False;
            curN = curN // 2;
        return True