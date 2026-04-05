class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0;
        nums.sort();
        i1 = 0;
        i2 = 1;
        result = 0;
        while i1 < len(nums)-1:
            while i2 < len(nums):
                total = nums[i1] + nums[i2];
                if total == k:
                    nums.pop(i2);
                    result += 1
                else:
                    i2 += 1
            i1 += 1;
            i2 = i1 + 1;
        return result

sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))