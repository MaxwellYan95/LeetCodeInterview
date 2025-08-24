class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        return max(self.maxSubArray(nums), self.withoutNeg(nums));

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

    def withoutNeg(self, nums: list[int]) -> int:
        total = sum(nums);
        maximum = total;
        newTotal = total;
        for i in range(len(nums)):
            if newTotal > (newTotal - nums[i]):
                maximum = max(newTotal, maximum);
                newTotal = total;
            else:
                newTotal -= nums[i];
        return maximum;

sol = Solution();
print(sol.withoutNeg([-2,4,-5,4,-5,9,4]))