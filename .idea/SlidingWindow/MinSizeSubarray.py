import statistics
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lower = 0;
        total = 0;
        minLen = sys.maxsize;
        for upper in range(len(nums)):
            total += nums[upper]
            while total >= target:
                minLen = min(upper-lower+1, minLen);
                total -= nums[lower]
                lower += 1
        if minLen == sys.maxsize:
            return 0;
        return minLen;

