class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1 for i in range(len(nums))]
        def recur(index: int) -> int:
            if index > len(nums)-1:
                return 0
            if dp[index] != -1:
                return dp[index];
            r1 = recur(index+1);
            r2 = nums[index] + recur(index+2);
            dp[index] = max(r1, r2);
            return dp[index]
        return recur(0);

