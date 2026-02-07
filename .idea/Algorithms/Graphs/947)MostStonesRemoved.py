from collections import defaultdict

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        self.neighbors = defaultdict(list)
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                x1, y1 = stones[i]
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    self.neighbors[(x1, y1)].append((x2, y2))
                    self.neighbors[(x2, y2)].append((x1, y1))
        self.visited = set();
        def dfs(x: int, y: int):
            if (x, y) in self.visited:
                return 1;
            self.visited.add((x,y))
            if len(self.neighbors[(x,y)]) == 0:
                return 1;
            result = 0;
            prevNeigh = self.neighbors[(x,y)]
            for x2, y2 in prevNeigh:
                result += dfs(x2, x1);
            return result+1;
        first = list(self.neighbors.keys())[0]
        return dfs(first[0], first[1])-1

sol = Solution()
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
