class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp = [[-float('inf') for i in range(len(nums)+1)] for j in range(len(nums))]
        allMulti = [[1 for i in range(len(nums)+1)] for j in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i+1] = nums[i];
        for i in range(len(nums)):
            multi = 1;
            for j in range(i+1, len(nums)+1):
                multi *= nums[j-1];
                allMulti[i][j] = multi;
        def recur(low: int, high: int):
            if dp[low][high] != -float('inf'):
                return dp[low][high];
            result = max(allMulti[low][high], recur(low+1, high), recur(low, high-1))
            dp[low][high] = result;
            return result
        return recur(0, len(nums));

sol = Solution();
print(sol.maxProduct([2,3,-2,4]))