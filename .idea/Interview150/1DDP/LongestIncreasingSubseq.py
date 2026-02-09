from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = defaultdict(int)
        dp[nums[0]] = 1;
        result = 1;
        for index in range(len(nums)):
            n = nums[index]
            dp[n] = 1
            for prev in nums[:index]:
                if prev < n:
                    dp[n] = max(dp[n], dp[prev] + 1);
                    result = max(result, dp[n])
        return result



sol = Solution();
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]));