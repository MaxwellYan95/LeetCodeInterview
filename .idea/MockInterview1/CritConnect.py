import collections


class Solution:

    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        self.visited = [False for i in range(n)]
        self.time = [-2 for i in range(n)]
        self.minTime = [-2 for i in range(n)]
        def makeGraph(n: int, connections: list[list[int]]) -> list[list[int]]:
            graph = [[] for i in range(n)]
            for connect in sorted(connections):
                x = connect[0];
                y = connect[1];
                graph[x].append(y);
                graph[y].append(x);
            return graph;

        self.g = makeGraph(n, connections);
        self.curTime = 0;
        self.bridges = [];
        def recur(node: int):
            self.time[node] = self.curTime;
            self.minTime[node] = self.time[node];
            self.curTime += 1;
            self.visited[node] = True;
            for adj in self.g[node]:
                if self.visited[adj] == False:
                    recur(adj);
                    self.minTime[adj] = min(self.minTime[node], self.minTime[adj])
            if (node != 0):
                if (self.minTime[node-1] < self.minTime[node]):
                    self.bridges.append([node, self.minTime[node]]);
        recur(0);
        return self.bridges;

sol = Solution();
print(sol.criticalConnections(4, [[0,1],[1,2],[2,1],[2,0],[1,3]]))
