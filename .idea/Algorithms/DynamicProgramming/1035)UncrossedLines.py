class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[-1 for i in range(len(nums2))] for j in range(len(nums1))]
        counter = 0
        if nums1[len(nums1)-1] == nums2[len(nums2)-1]:
            dp[len(nums1)-1][len(nums2)-1] = 1
        else:
            dp[len(nums1)-1][len(nums2)-1] = 0
        def recur(bound1: int, bound2: int):
            if bound1 > len(nums1)-1 or bound2 > len(nums2)-1:
                return 0;
            if dp[bound1][bound2] != -1:
                return dp[bound1][bound2];
            result = -1;
            if nums1[bound1] == nums2[bound2]:
                result = max(result, 1+recur(bound1+1, bound2+1))
            result = max(result, recur(bound1, bound2+1), recur(bound1+1, bound2))
            dp[bound1][bound2] = result;
            return dp[bound1][bound2]
        result = recur(0, 0)
        return result
sol = Solution()
print(sol.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
print()