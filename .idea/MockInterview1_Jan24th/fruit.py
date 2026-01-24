from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length = 0;
        maxLen = 0;
        types = []
        for index in range(len(fruits)):
            curFruit = fruits[index];
            if len(types) == 2 and curFruit not in types:
                maxLen = max(maxLen, length);
                length = 0;
                types = types[1:]
                types.append(curFruit);
                continue;
            if curFruit not in types:
                types.append(curFruit);
            length += 1;
        maxLen = max(maxLen, length);
        return maxLen

sol = Solution()
print(sol.totalFruit([0,1,2,2]))

