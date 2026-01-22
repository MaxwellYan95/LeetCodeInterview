from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        slices = defaultdict(int)
        if len(nums) <= 1:
            return 0;
        for i in range(len(nums)-1):
            slices[nums[i]-nums[i+1]] += 1;
        for begin in range(len(nums)-2):
            diff = nums[begin]-nums[begin+1]
            for end in range(begin+2, len(nums)):
                newDiff = nums[end-1]-nums[end]
                if diff != newDiff:
                    break;
                else:
                    slices[diff] += 1;