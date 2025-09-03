from collections import defaultdict
class Solution:
    def makeDict(self, prerequisites: list[list[int]]):
        graph = defaultdict(list);
        for c1, c2 in prerequisites:
            graph[c1].append(c2);
        return graph;

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preqDict = self.makeDict(prerequisites);
        visited = [];
        def dfs(course: int):
            # Dont put "course in visited" first
            if course in visited:
                return False;
            if not preqDict[course]:
                return True;
            visited.append(course);
            for subCourse in preqDict[course]:
                if not dfs(subCourse):
                    return False;
            preqDict.pop(course);
            return True;
        for course in range(numCourses):
            if not dfs(course):
                return False;
        return True;

sol = Solution();
print(sol.canFinish(2, [[1,0],[0,1]]));
print(sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]));
print(sol.canFinish(3, [[0,1],[0,2],[1,2]]));
