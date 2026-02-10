class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        pow = 0;
        results = self.countBits(n-1)
        while 2**pow <= n:
            pow += 1
        ones = 0;
        newN = n;
        while newN != 0:
            if 2**pow <= newN:
                newN -= 2**pow;
                ones += 1;
            pow -= 1
        results.append(ones);
        return results