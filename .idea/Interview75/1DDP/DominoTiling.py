class Solution:
    def numTilings(self, n: int) -> int:
        """
        Formula:
        if n % 3 == 0:
            dp[n] = dp[n-1] + dp[n-2] + 2*dp[n-3]
        else:
            dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

        Example: n = 5
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 5;
        dp[4] = dp[1] + dp[2] + dp[]

        :param n:
        :return:
        """

        # Parameter: prev val n

        dp = [-1 for i in range(n)]
        for i in range(2, n):
            for j in range(i):
                dp[i] += (dp[j] + 1)
        return dp[len(dp)-1]
