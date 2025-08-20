class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target <= nums[0]:
            return 0;
        elif target == nums[len(nums)-1]:
            return len(nums)-1;
        elif target > nums[len(nums)-1]:
            return len(nums);
        halfLen = int((len(nums)-1)/2);
        halfLenPlus = halfLen + 1;
        firstNum = nums[halfLen];
        secondNum = nums[halfLenPlus];
        if firstNum == target:
            return halfLen;
        elif secondNum == target:
            return halfLenPlus
        elif secondNum < target:
            return self.searchInsert(nums[halfLenPlus+1:], target)+halfLenPlus+1;
        elif firstNum > target:
            return self.searchInsert(nums[:halfLen], target);
        else:
            return halfLenPlus;




sol = Solution()
sol.searchInsert([2,3,5,6,9], 7)
