class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0;
        zeroes = 0;
        length = len(nums)
        while index < length-zeroes:
            if nums[index] == 0:
                nums.pop(index);
                nums.append(0);
                zeroes += 1;
            else:
                index += 1;
sol = Solution()
print(sol.moveZeroes([0,0,1]))