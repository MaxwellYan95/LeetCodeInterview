from collections import defaultdict;

class Solution:
    def solveLine(self, point1: list[int], point2: list[int]):
        if (point2[0] - point1[0]) == 0:
            return ""
        m = (point2[1] - point1[1]) / (point2[0] - point1[0]);
        b = point1[1] - m * point1[0];
        return str(m) + " " + str(b);

    def maxPoints(self, points: list[list[int]]) -> int:
        lines = defaultdict(int);
        ans = 0;
        for i1 in range(len(points)):
            for i2 in range(i1+1, len(points)):
                p1 = points[i1];
                p2 = points[i2];
                key = self.solveLine(p1, p2);
                if key == "":
                    continue;
                lines[key] += 1;
                ans = max(ans, lines[key]);
        return ans;

sol = Solution();
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]));