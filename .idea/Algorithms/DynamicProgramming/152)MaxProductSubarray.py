class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp = [-float('inf') for i in range(len(nums)+1)];
        dp[0] = max(dp[0], nums[0])
        multi = [[0 for i in range(len(nums)+1)] for j in nums]
        for index in range(len(nums)):
            multi[index][index+1] = nums[index];
            dp[index+1] = max(dp[index+1], multi[index][index+1])
        for low in range(len(nums)):
            for high in range(low+2, len(nums)+1):
                multi[low][high] = multi[low][high-1] * nums[high-1];
                dp[high] = max(dp[high-1], dp[high], multi[low][high])
        return dp[len(nums)];

sol = Solution();
print(sol.maxProduct([2,3,-2,4]))