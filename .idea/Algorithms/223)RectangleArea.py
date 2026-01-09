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
        xInter = False;
        yInter = False;
        for point in aPoints:
            xCoord = point[0];
            b1 = bPoints[0][0];
            b2 = bPoints[1][0];
            if b1 < xCoord < b2:
                xInter = True;
            if b2 < xCoord < b1:
                xInter = True;
        for point in bPoints:
            xCoord = point[0];
            a1 = aPoints[0][0];
            a2 = aPoints[1][0];
            if a1 < xCoord < a2:
                xInter = True;
            if a2 < xCoord < a1:
                xInter = True;
        for point in aPoints:
            yCoord = point[1];
            b1 = bPoints[0][1];
            b2 = bPoints[1][1];
            if b1 < yCoord < b2:
                yInter = True;
            if b2 < yCoord < b1:
                yInter = True;
        for point in bPoints:
            yCoord = point[1];
            a1 = aPoints[0][1];
            a2 = aPoints[1][1];
            if a1 < yCoord < a2:
                yInter = True;
            if a2 < yCoord < a1:
                yInter = True;
        return xInter and yInter;

sol = Solution();
area = sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2);
print()