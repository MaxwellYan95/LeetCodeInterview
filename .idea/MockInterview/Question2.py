import collections


class Solution:

    def removeEdge(self, edge: list[int], points: dict):
        edge1 = edge[0];
        edge2 = edge[1];
        if edge1 in points:
            points[edge1].remove(edge2);
        if edge2 in points:
            points[edge2].remove(edge1);

    def addEdge(self, edge: list[int], points: dict):
        edge1 = edge[0];
        edge2 = edge[1];
        if edge1 not in points:
            points[edge1] = [edge2];
        else:
            points[edge1].append(edge2);
        if edge2 not in points:
            points[edge2] = [edge1];
        else:
            points[edge2].append(edge1);

    def connectDict(self, n: int, connections: list[list[int]]):
        points = {};
        for connect in connections:
            self.addEdge(connect, points);
        return points;

    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        dictionary = self.connectDict(n, connections);
        critical = [];
        for connect in connections:
            visited = [];
            def bfs(points: dict):
                q = collections.deque();
                q.append(0);
                while q:
                    node = q.popleft();
                    if node in points:
                        for neigh in points[node]:
                            if neigh not in visited:
                                visited.append(neigh);
                                q.append(neigh);
                if len(visited) == n:
                    return False;
                return True;
            self.removeEdge(connect, dictionary);
            isCrit = bfs(dictionary);
            self.addEdge(connect, dictionary);
            if (isCrit):
                critical.append(connect);
        return critical;

sol = Solution();
print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
