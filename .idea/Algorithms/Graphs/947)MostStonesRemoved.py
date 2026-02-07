from collections import defaultdict

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        self.neighbors = defaultdict(list)
        self.points = []
        for i in range(len(stones)):
            x1, y1 = stones[i]
            for j in range(i+1, len(stones)):
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    self.neighbors[(x1, y1)].append((x2, y2))
                    self.neighbors[(x2, y2)].append((x1, y1))
            self.points.append((x1, y1))
        self.visited = set();
        def dfs(x: int, y: int):
            self.visited.add((x,y))
            for x2, y2 in self.neighbors[(x,y)]:
                if (x2, y2) not in self.visited:
                    dfs(x2, y2)

        component = 0;
        for p in self.points:
            if p not in self.visited:
                dfs(p[0], p[1]);
                component += 1;

        # Find all connected components
        # You have to keep 1 node from each connected component
        return len(stones) - component

sol = Solution()
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
