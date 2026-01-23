from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        nodeLst = [i for i in range(n)];
        neighbor = defaultdict(list)
        for p1, p2 in edges:
            neighbor[p1].append(p2)
            neighbor[p2].append(p1)
        while len(nodeLst) > 2:
            removeLst = []
            for node in nodeLst:
                if len(neighbor[node]) == 1:
                    nextNode = neighbor[node][0];
                    neighbor[nextNode].remove(node)
                    neighbor[node].remove(nextNode)
                    removeLst.append(node);
            for node in removeLst:
                nodeLst.remove(node)
        return nodeLst


sol = Solution()
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
