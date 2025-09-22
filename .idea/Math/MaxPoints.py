from collections import defaultdict;

class Solution:
    def solveLine(self, p1: list[int], p2: list[int]):
        if p2[0]-p1[0] == 0:
            return None;
        m = float((p2[1]-p1[1])/(p2[0]-p1[0]))
        b = p2[1] - m*p2[0];
        return (m, b);

    def maxPoints(self, points: list[list[int]]) -> int:
        pointDict = defaultdict(list);
        points.sort();
        for i1 in range(len(points)-1):
            for i2 in range(i1+1, len(points)):
                print("(" + str(points[i1][0]) + ", " + str(points[i1][1]) + "), "
                      + "(" + str(points[i2][0]) + ", " + str(points[i2][1]) + "), ")
                line = self.solveLine(points[i1], points[i2]);
                if line != None:
                    if points[i1] not in pointDict[line]:
                        pointDict[line].append(points[i1]);
                    if points[i2] not in pointDict[line]:
                        pointDict[line].append(points[i2]);
        maximum = 0;
        for key in pointDict.keys():
            maximum = max(len(pointDict[key]), maximum);
        return maximum;

sol = Solution();
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]));