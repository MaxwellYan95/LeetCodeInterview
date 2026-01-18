class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0;
        power = 0;
        while 2**power < n:
            power += 1;
        curN = n;
        while curN != 0:
            if curN >= 2**power:
                ones += 1
                curN -= 2**power
            power -= 1;
        return ones;

sol = Solution();
print(sol.hammingWeight(11))