class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        maxRes = -float('inf');
        lst = nums.copy();
        for i in range(len(nums)):
            lst = lst[len(lst)-1:] + lst[:len(lst)-1]
            res = 0;
            for index in range(len(lst)):
                res += (index*lst[index]);
            maxRes = max(res, maxRes);
        return maxRes;
