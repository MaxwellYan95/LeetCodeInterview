class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = abs(ax1 - ax2) * abs(ay1 - ay2);
        areaB = abs(bx2 - bx1) * abs(by1 - by2);
        interArea = 0;
        isIntersect = self.isOverlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        if isIntersect:
            xLst = [ax1, ax2, bx1, bx2];
            yLst = [ay1, ay2, by1, by2];
            xLst.sort()
            yLst.sort()
            xDiff = abs(xLst[1] - xLst[2]);
            yDiff = abs(yLst[1] - yLst[2]);
            interArea = xDiff * yDiff;

        return areaA + areaB - interArea;

    def isOverlap(self, ax1: int, ay1: int, ax2: int, ay2: int,
                  bx1: int, by1: int, bx2: int, by2: int) -> bool:
        aPoints = [[ax1, ay1], [ax2, ay2]]
        bPoints = [[bx1, by1], [bx2, by2]]
        xyInter = [False, False];
        for p in range(0, 2):
            for xy in range(0, 2):
                pA = aPoints[p][xy]
                pB = bPoints[p][xy]
                a1 = aPoints[0][xy]
                a2 = aPoints[1][xy]
                b1 = bPoints[0][xy]
                b2 = bPoints[1][xy]
                if b2 <= pA <= b1:
                    xyInter[xy] = True;
                if b1 <= pA <= b2:
                    xyInter[xy] = True;
                if a2 <= pB <= a1:
                    xyInter[xy] = True;
                if a1 <= pB <= a2:
                    xyInter[xy] = True;
        return xyInter[0] and xyInter[1];

sol = Solution();
area = sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2);
print()