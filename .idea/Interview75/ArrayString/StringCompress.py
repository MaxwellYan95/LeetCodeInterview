from collections import defaultdict

class Solution:
    def compress(self, chars: list[str]) -> int:
        countDict = dict();
        for c in chars:
            if c not in countDict:
                countDict[c] = 1;
            else:
                countDict[c] += 1;
        result = "";
        for k in countDict.keys():
            result += str(k)
            if countDict[k] > 1:
                result += str(countDict[k])
        return len(result)

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))
