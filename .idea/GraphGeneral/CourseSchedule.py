import collections

class Solution:
    def makeDict(self, prerequisites: list[list[int]]):
        graph = dict();
        for c1, c2 in prerequisites:
            if c1 not in graph:
                graph[c1] = [[c1, c2]];
            else:
                graph[c1].append([c1, c2]);
        return graph;

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preqDict = self.makeDict(prerequisites);
        visited = [];
        def dfs(edge: list[int]):
            course = edge[1];
            if course in visited:
                return False;
            visited.append(course);
            if course not in preqDict:
                return True;
            for nextEdge in preqDict[course]:
                result = dfs(nextEdge);
                if result == False:
                    return False;
            return True;
        for key in preqDict.keys():
            for edge in preqDict[key]:
                res = dfs(edge);
                if res == False:
                    return False;
                visited = [];
        return True;

sol = Solution();
print(sol.canFinish(2, [[1,0],[0,1]]));
print(sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]));
