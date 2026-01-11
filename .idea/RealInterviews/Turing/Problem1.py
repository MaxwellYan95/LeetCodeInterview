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

import numpy as np;

class Solution:

    dp = np.array([[-1 for inner in range(len(nums))] for outer in range(len(nums))])

    def longestArithSeqLength(self, nums: list[int]) -> int:
        diffs = [];
        longest = 0;
        for i in range(len(nums)):
            self.dp[i][i] = 0;
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                self.dp[i][j] = nums[j] - nums[i];
                if self.dp[i][j] not in diffs:
                    diffs.append(self.dp[i][j]);

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if self.dp[i][j] in diffs:
                    longest = max(longest, self.bfs(j, j, self.dp[i][j]));
                    diffs.remove(self.dp[i][j]);


    def bfs(self, row: int, col: int, diff: int):
        result = 0;
        subDP = dp[row:, col:]
        if len(subDP) == 0:
            return 0;
        for index in len(subDP[0]):
            n = subDP[0][index];
            if n == diff:
                result = max(result, self.bfs(index, index, diff))
        return result;

sol = Solution()
print(sol.longestArithSeqLength([3,6,9,12]))