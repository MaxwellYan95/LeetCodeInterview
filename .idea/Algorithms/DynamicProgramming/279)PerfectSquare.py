class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1 for i in range(n+1)];
        num = 1;
        allSquares = []
        while num*num <= n:
            dp[num*num] = 1;
            allSquares.append(num*num)
            num += 1;
        if dp[n] != -1:
            return dp[n];
        def recur(i: int) -> int:
            if dp[i] != -1:
                return dp[i];
            minNum = float('inf')
            for sqrt in allSquares:
                if sqrt < i:
                    minNum = min(minNum, recur(sqrt) + recur(i-sqrt));
            dp[i] = minNum;
            return dp[i];
        return recur(n)
sol = Solution()
print(sol.numSquares(2))