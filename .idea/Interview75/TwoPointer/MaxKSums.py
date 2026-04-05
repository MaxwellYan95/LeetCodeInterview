class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        first = 0;
        last = len(nums)-1;
        result = 0
        total = nums[first] + nums[last]
        while last > first:
            if k == total:
                first += 1;
                last -= 1;
                result += 1
            elif total > k:
                last -= 1;
            elif total < k:
                first += 1;
            total = nums[first] + nums[last]
        return result
sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))

