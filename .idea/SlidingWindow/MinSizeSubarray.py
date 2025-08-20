import statistics
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0;
        sum = 0;
        minLen = sys.maxsize;
        for right in range(len(nums)):
            sum += nums[right];
            while sum >= target:
                minLen = min(minLen, right-left+1);
                sum -= nums[left];
                left += 1;
        if minLen == sys.maxsize:
            return 0;
        return minLen;

