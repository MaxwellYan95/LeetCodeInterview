class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = (len(nums)-(k%len(nums)))
        leftNums = nums[:rotate];
        rightNums = nums[rotate:];
        index = 0;
        for right in rightNums:
            nums[index] = right;
            index += 1;
        for left in leftNums:
            nums[index] = left;
            index += 1;


sol = Solution();
sol.rotate([1,2,3,4,5,6,7], 3)