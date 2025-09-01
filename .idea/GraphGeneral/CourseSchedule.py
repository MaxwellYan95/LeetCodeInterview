import collections

class Solution:
    def makeDict(self, prerequisites: list[list[int]]):
        graph = dict();
        for c1, c2 in prerequisites:
            if c1 not in graph:
                graph[c1] = [c2];
            else:
                graph[c1].append(c2);
        return graph;

    def bfs(self, preqDict: dict):
        if len(preqDict.keys()) == 0:
            return True;
        stack = collections.deque();
        stack.append(list(preqDict.keys())[0]);
        visited = [];
        while stack:
            course = stack.popleft();
            for subCourse in preqDict[course]:
                if subCourse in visited:
                    return False;
                stack.append(subCourse);
                visited.append(subCourse);
        return True;

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preqDict = self.makeDict(prerequisites);
        return self.bfs(preqDict);

sol = Solution();
print(sol.canFinish(2, [[1,0]]));
