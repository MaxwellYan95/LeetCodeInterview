class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0;
        for index in range(len(nums)):
            rightSum -= nums[index];
            if rightSum == leftSum:
                return index
            leftSum += nums[index];
        return -1

sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))