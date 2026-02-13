from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        diff = [nums[index]-nums[index+1] for index in range(len(nums)-1)]
        count = [0 for index in range(len(nums)-1)]
        for i in range(1, len(nums)-1):
            if (diff[i-1] == diff[i]):
                count[i] = count[i-1]+1;
        return sum(count)