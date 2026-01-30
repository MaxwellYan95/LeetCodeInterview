from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        # adj matrix with direction
        self.richLst = defaultdict(list)
        for value, key in richer:
            self.richLst[key].append(value)
        def bfs(start: int):
            stack = [start];
            minQuiet = float('inf')
            end = 0;
            visited = [False for i in range(len(quiet))]
            while stack:
                node = stack.pop();
                if minQuiet > quiet[node]:
                    minQuiet = quiet[node];
                    end = node
                visited[node] = True
                for neigh in self.richLst[node]:
                    if visited[neigh] == False:
                        stack.append(neigh)
            return end;
        result = [];
        for index in range(len(quiet)):
            result.append(bfs(index))
        return result




