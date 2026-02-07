from collections import defaultdict

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        self.visited = [];
        result = 0;
        for index in range(len(stones)):
            s1 = stones[index]
            self.visited.append(s1)
            if s1 in self.visited:
                neighbor = 0;
                recent = s1;
                for s2 in stones[index+1:]:
                    if recent[0] == s2[0] or recent[0] == s2[0]:
                        neighbor += 1;
                        recent = s2;
                        self.visited.append(s2)
                result += neighbor
        return result

sol = Solution()
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
