from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        length = 0;
        maxLen = 0;
        # stores type and most recent index
        types = {}

        start = 0;
        for index in range(len(fruits)):
            curFruit = fruits[index];
            if len(types) == 2 and curFruit not in types:
                keyLst = list(types.keys());
                if types[keyLst[0]] > types[keyLst[1]]:
                    start = types[keyLst[1]] + 1;
                    types.pop(keyLst[1])
                else:
                    start = types[keyLst[0]] + 1;
                    types.pop(keyLst[0])
            types[curFruit] = index
            maxLen = max(maxLen, index - start + 1);
        return maxLen

sol = Solution()
print(sol.totalFruit([0,1,2,2]))

