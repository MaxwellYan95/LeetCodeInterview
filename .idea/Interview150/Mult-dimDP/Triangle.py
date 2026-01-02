class Solution:

    dataDict = {};

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1 and len(triangle[0]) == 1:
            return triangle[0][0];
        allZero = False;
        left = [];
        right = [];
        for row in triangle[1:]:
            left.append(tuple(row[:len(row)-1]));
            right.append(tuple(row[1:]));
        leftWay = 0;
        rightWay = 0;
        if tuple(left) in self.dataDict.keys():
            leftWay = triangle[0][0] + self.dataDict[tuple(left)];
        else:
            newKey = tuple(left);
            newValue = self.minimumTotal(left);
            leftWay = triangle[0][0] + newValue;
            self.dataDict[newKey] = newValue;
        if tuple(right) in self.dataDict.keys():
            rightWay = triangle[0][0] + self.dataDict[tuple(right)];
        else:
            newKey = tuple(right);
            newValue = self.minimumTotal(right);
            rightWay = triangle[0][0] + newValue;
            self.dataDict[newKey] = newValue;
        return min(leftWay, rightWay);



