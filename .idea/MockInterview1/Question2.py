import collections


class Solution:

    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        adjMatrix = [[0 for i in range(n)] for j in range(n)]
        for connect in connections:
            if connect[1] > connect[0]:
                adjMatrix[connect[0]][connect[1]] = 1
            else:
                adjMatrix[connect[1]][connect[0]] = 1
        crits = [];
        for x in range(n):
            for y in range(x+1, n):
                xAdj = [adjMatrix[index][y] for index in range(0, n)]
                yAdj = [adjMatrix[x][index] for index in range(0, n)]
                if adjMatrix[x][y] == 1 and sum(xAdj) == 1 and sum(yAdj) == 1:
                    crits.append([x, y]);
        return crits;

    def hasAdjOne(self, x: int, y: int, adjMatrix: list[list[int]]):
        for xAdj in [x-1, x+1]:
            bounds = xAdj >= 0 or xAdj < len(adjMatrix);
            if bounds:
                if adjMatrix[xAdj][y] == 1:
                    return True;
        for yAdj in [y-1, y+1]:
            bounds = yAdj >= 0 or yAdj < len(adjMatrix);
            if bounds:
                if adjMatrix[x][yAdj] == 1:
                    return True;
        return False;

sol = Solution();
print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
