from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        slices = []
        if len(nums) <= 1:
            return 0;
        for i in range(len(nums)-1):
            slices.append(nums[i]-nums[i+1]);
        prevSlice = slices[0]
        count = [0 for i in range(len(nums))]
        for i in range(1, len(slices)):
            if slices[i] == prevSlice:
                count[i+1] = count[i]+1;
            else:
                count[i+1] = 0;
            prevSlice = slices[i]
        return sum(count)
