class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        self.neighbors = {}
        for i in range(n):
            self.neighbors[i] = []
        for edge in edges:
            u = edge[0]
            v = edge[1]
            self.neighbors[u].append(v)
            self.neighbors[v].append(u)
        self.visited = [False for i in range(n)]
        self.minHeight = float('inf')
        self.map = {} # root: height
        def dfs(n: int):
            maximum = 0;
            self.visited[n] = True;
            for next in self.neighbors[n]:
                if self.visited[next] == False:
                    maximum = max(maximum, dfs(next))
            return maximum + 1;
        for node in range(n):
            self.visited = [False for i in range(n)]
            height = dfs(node);
            self.minHeight = min(self.minHeight, height);
            self.map[node] = height;
        result = [];
        for root in range(n):
            if self.map[root] == self.minHeight:
                result.append(root);
        return result

sol = Solution()
print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))
