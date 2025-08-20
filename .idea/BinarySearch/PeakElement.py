class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0;
        if nums[0] > nums[1]:
            return 0;
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1;
        leftIndex = 1;
        rightIndex = len(nums)-2;
        while (leftIndex < rightIndex):
            if nums[rightIndex] > nums[rightIndex+1] and nums[rightIndex] > nums[rightIndex-1]:
                return rightIndex;
            else:
                rightIndex = rightIndex - 1;
            if nums[leftIndex] > nums[leftIndex+1] and nums[leftIndex] > nums[leftIndex-1]:
                return leftIndex;
            else:
                leftIndex = leftIndex + 1;
        return leftIndex;
