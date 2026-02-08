class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        dict = {}
        pairs.sort(key=lambda x: x[1])
        dict[pairs[0][1]] = 1
        maxLen = 1;
        for c, d in pairs[1:]:
            newDict = {}
            newDict[d] = 0 if d not in dict else dict[d]
            for b in dict:
                if b < c:
                    newDict[d] = max(newDict[d], dict[b] + 1);
            dict.update(newDict)
            if d not in dict:
                dict[d] = 1;
            maxLen = max(maxLen, dict[d])
        return maxLen

sol = Solution()
print(sol.findLongestChain([[9,10],[9,10],[4,5],[-9,-3],[-9,1],[0,3],[6,10],[-5,-4],[-7,-6]]))
