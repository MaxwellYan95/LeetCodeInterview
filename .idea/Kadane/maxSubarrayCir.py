class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = sum(nums);
        maximum = self.maxSubArray(nums);
        minimum = self.minSubArray(nums);
        if total-minimum <= 0:
            return maximum;
        return max(maximum, total-minimum);

    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0];
        sum = 0;
        for i in range(len(nums)):
            sum += nums[i];
            if sum > res:
                res = sum;
            if sum < 0:
                sum = 0;
        return res;

    def minSubArray(self, nums: list[int]) -> int:
        res = nums[0];
        sum = 0;
        for i in range(len(nums)):
            sum += nums[i];
            if sum < res:
                res = sum;
            if sum > 0:
                sum = 0;
        return res;

sol = Solution();
print(sol.maxSubarraySumCircular([-2,4,-5,4,-5,9,4]));
print(sol.maxSubarraySumCircular([-3,-2,-3]));