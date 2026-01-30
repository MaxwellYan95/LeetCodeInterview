class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i1 in range(len(nums)):
            n1 = nums[i1]
            for i2 in range(i1+1, len(nums)):
                n2 = nums[i2]
                if n2 + n1 == target:
                    return [i1, i2]
        return []

sol = Solution()
print(sol.twoSum([3,2,4], 6))
