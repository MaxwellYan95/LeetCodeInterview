class Solution:
    def numTilings(self, n: int) -> int:
        """
        Formula:
        if n % 3 == 0:

        else:
            dp[n] = (dp[n-1]+1) + (dp[n-2]+1)


        :param n:
        :return:
        """

        # Parameter: prev val n

        dp = [-1 for i in range(n)]
        for i in range(2, n):
            for j in range(i):
                dp[i] += (dp[j] + 1)
        return dp[len(dp)-1]
