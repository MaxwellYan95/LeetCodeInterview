class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        adjMatrix = [[0 for i in range(n)] for j in range(n)]
        for edge in edges:
            adjMatrix[edge[0]][edge[1]] = 1;
            adjMatrix[edge[1]][edge[0]] = 1;
        self.visited = [False for i in range(n)]
        self.minHeight = float('inf')
        self.map = {} # root: height
        def bfs(n: int):
            height = 0;
            stack = [n];
            while stack:
                current = stack.pop();
                self.visited[current] = True;
                for neighbor in adjMatrix[current]:
                    if self.visited[neighbor] == False:
                        stack.append(neighbor);
                height += 1;
            self.minHeight = min(self.minHeight, height);
            map[n] = height;
        for node in range(n):
            bfs(node);
        result = [];
        for root in range(n):
            if map[root] == self.minHeight:
                result.append(root);
        return result

sol
