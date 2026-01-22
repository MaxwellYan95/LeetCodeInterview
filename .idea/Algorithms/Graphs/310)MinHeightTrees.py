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
                addedNode = False;
                for index in range(len(adjMatrix[current])):
                    isNeighbor = adjMatrix[current][index] == 1
                    if self.visited[index] == False and isNeighbor:
                        stack.append(index);
                        addedNode = True
                if addedNode:
                    height += 1;
            self.minHeight = min(self.minHeight, height);
            self.map[n] = height;
        for node in range(n):
            self.visited = [False for i in range(n)]
            bfs(node);
        result = [];
        for root in range(n):
            if self.map[root] == self.minHeight:
                result.append(root);
        return result

sol = Solution()
print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))
