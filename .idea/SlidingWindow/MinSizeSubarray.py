import statistics
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lower = 0;
        upper = 1;
        total = 0;
        minLen = sys.maxsize;
        while lower != upper and upper <= len(nums):
            window = nums[lower:upper];
            total = sum(window)
            if total < target:
                upper += 1
            else:
                minLen = min(upper-lower, minLen)
                lower += 1
        if minLen == sys.maxsize:
            return 0;
        return minLen;

sol = Solution()
print(sol.minSubArrayLen(4, [1,4,4]))


