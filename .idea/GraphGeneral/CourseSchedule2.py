from collections import defaultdict
class Solution:
    def makeDict(self, prerequisites: list[list[int]]):
        graph = defaultdict(list);
        for c1, c2 in prerequisites:
            graph[c1].append(c2);
        return graph;

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preqDict = self.makeDict(prerequisites);
        visited = [];
        def dfs(course: int):
            lst = []
            if not preqDict[course]:
                return [course];
            # "course in visited" comes 2nd
            if course in visited:
                return [];
            visited.append(course);
            for subCourse in preqDict[course]:
                prevList = dfs(subCourse);
                if len(prevList) == 0:
                    return [];
                lst.extend(prevList);
            lst.insert(len(lst)-1, course);

            # pop() is used as memorization
            preqDict.pop(course);
            return lst;
        for course in range(numCourses):
            lst = dfs(course)
            if not lst:
                return [];
        return visited;
sol = Solution();
print(sol.findOrder(2, [[1,0],[0,1]]));
print(sol.findOrder(5, [[1,4],[2,4],[3,1],[3,2]]));
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(3, [[0,1],[0,2],[1,2]]));