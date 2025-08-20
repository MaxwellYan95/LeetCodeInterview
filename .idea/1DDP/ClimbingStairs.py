class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2;
        elif n == 3:
            return 3;
        return self.climbStairs(n-1) + 1;

sol = Solution();
print(sol.climbStairs(4));