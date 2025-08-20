class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        while nums[0] > nums[1]:
            nums = nums[1:];
        while nums[len(nums)-2] > nums[len(nums)-1]:
            nums = nums[:len(nums)-1];
        i = 1;
        while True:
            cond = (num[i-1] > nums[i]) or (num[i] > nums[i+1]);
            if cond:
                nums = nums[:i] + nums[i+1:];
            else:
                i += 1;
            if i == len(nums)-1:
                break;
        return len(nums);
