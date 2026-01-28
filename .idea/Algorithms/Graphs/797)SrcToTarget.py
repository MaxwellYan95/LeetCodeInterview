from collections import defaultdict

class Solution:

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # Using Dijstrka Alg
        self.stack = []
        indexes = [i for i in range(len(graph))]
        self.stack.append(0);
        self.mapping = defaultdict(list)
        self.mapping[0] = [[0]]
        def djstrka():
            for node in range(len(graph)):
                nodePaths = self.mapping[node]
                for neighbor in graph[node]:
                    newPaths = [nodePaths[i]+[neighbor] for i in range(len(nodePaths))]
                    self.mapping[neighbor].extend(newPaths);
                    self.stack.append(neighbor)
        djstrka()
        if len(self.mapping[len(graph)-1]) == 0:
            djstrka()
        return self.mapping[len(graph)-1];

sol = Solution()
print(sol.allPathsSourceTarget([[2],[3],[1],[]]))

