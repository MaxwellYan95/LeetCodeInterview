import statistics
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        lower = 0;
        upper = 1;
        total = 0;
        minLen = sys.maxsize;
        while lower != upper and upper <= len(nums):
            window = nums[lower:upper];
            if total < target:
                total += nums[upper-1]
                upper += 1
            else:
                while total >= target and lower != upper:
                    minLen = min(upper-lower, minLen)
                    total -= nums[lower]
                    lower += 1
        if minLen == sys.maxsize:
            return 0;
        return minLen;

sol = Solution()
print(sol.minSubArrayLen(4, [1,4,4]))


