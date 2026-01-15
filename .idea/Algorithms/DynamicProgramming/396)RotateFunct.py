class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        maxRes = -float('inf');
        total = sum(nums)
        n = len(nums)
        res = 0;
        for index in range(n):
            res += (index*nums[index]);
        maxRes = max(maxRes, res);
        for index in range(n):
            res += total;
            res -= (n*nums[n-1-index]);
            maxRes = max(maxRes, res);
        return maxRes