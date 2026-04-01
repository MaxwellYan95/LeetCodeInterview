class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dpDict = {}
        result = 1
        for num in arr:
            prevNum = num - difference;
            if prevNum not in dpDict:
                dpDict[num] = 1;
            else:
                dpDict[num] = dpDict[prevNum]+1;
            result = max(result, dpDict[num])
        return result

sol = Solution()
print(sol.longestSubsequence([1,2,3,4], 1))