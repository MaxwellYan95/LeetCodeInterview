class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        maxResult = sum([nums[index]*index for index in range(len(nums))])
        num = maxResult;
        allNum = sum(nums)
        for n in reversed(nums):
            num += allNum;
            num -= len(nums)*n;
            maxResult = max(maxResult, num);
        return maxResult;
