class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[0 for i in range(len(nums2))] for j in range(len(nums1))]
        counter = 0;
        if nums1[0] == nums2[0]:
            counter = 1;
        for i1 in range(len(nums1)):
            dp[i1][0] = counter;
        for i2 in range(len(nums2)):
            dp[0][i2] = counter;
        for i1 in range(1, len(nums1)):
            add = 0;
            for i2 in range(1, len(nums2)):
                dp[i1][i2] = dp[i1-1][i2-1];
                if nums1[i1] == nums2[i2]:
                    add = 1;
                dp[i1][i2] += add

        return dp[len(nums1)-1][len(nums2)-1]
sol = Solution()
print(sol.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))