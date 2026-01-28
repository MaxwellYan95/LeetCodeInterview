from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # finding degrees of each node
        neighbor = defaultdict(list)
        stack = [i for i in range(n)]
        for u, v in edges:
            neighbor[u].append(v);
            neighbor[v].append(u);
        while len(stack) > 2:
            oneDegree = [];
            for node in stack:
                degree = len(neighbor[node])
                if degree == 1:
                    oneDegree.append(node)
            for node in oneDegree:
                adj = neighbor[node][0]
                neighbor[adj].remove(node)
                neighbor.pop(node);
                stack.remove(node)
        return stack



sol = Solution()
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
