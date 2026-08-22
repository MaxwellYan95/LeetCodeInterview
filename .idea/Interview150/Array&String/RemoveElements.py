class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0;
        count = len(nums);
        while index < len(nums):
            value = nums[index];
            if value == val:
                count -= 1;
                nums.pop(index);
                nums.append(-1);
            else:
                index += 1;
        return count;

sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))