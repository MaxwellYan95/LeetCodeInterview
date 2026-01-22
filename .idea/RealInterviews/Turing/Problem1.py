"""
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:
========================================
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Example 1:
========================================
Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
========================================
Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

Example 3:
========================================
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].
"""
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        # dp[end_index][diff] = size of longest arithmetic sequence
        dp = [{} for i in range(len(nums))]
        longestArr = 0;
        for cur_index in range(len(nums)-1):
            for next_index in range(cur_index+1, len(nums)):
                diff = nums[cur_index]-nums[next_index];
                if diff not in dp[cur_index]:
                    dp[next_index][diff] = 1+1;
                else:
                    dp[next_index][diff] = 1+dp[cur_index][diff]
                longestArr = max(longestArr, dp[next_index][diff]);
        return longestArr


sol = Solution()
print(sol.longestArithSeqLength([83,20,17,43,52,78,68,45]))