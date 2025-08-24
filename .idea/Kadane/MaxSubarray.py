class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        index = 0;
        res = nums[0];
        curSum = 0;
        for i in range(len(nums)):
            curSum += nums[i];
            if curSum > res:
                res = curSum;
            if curSum < 0:
                curSum = 0;
        return res;


sol = Solution();
print(sol.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]));
