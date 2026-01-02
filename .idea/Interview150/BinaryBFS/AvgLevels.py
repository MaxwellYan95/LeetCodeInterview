class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        levelLst = self.extractLevelList(root)
        result = []
        for lst in levelLst:
            avg = sum(lst) / len(lst)
            result.append(avg)
        return result

    def extractLevelList(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root == None:
            return 0;
        result = [];
        leftLst = [];
        rightLst = [];
        if root.left != None:
            leftLst = self.extractLevelList(root.left);
        if root.right != None:
            rightLst = self.extractLevelList(root.right);
        greaterLst = [];
        index = 0;
        if len(leftLst) > len(rightLst):
            index = len(rightLst);
            greaterLst = leftLst[index:];
        else:
            index = len(leftLst);
            greaterLst = rightLst[index:];
        result.append([root.val]);
        for i in range(0, index):
            lst = leftLst[i] + rightLst[i]
            result.append(lst);
        result.extend(greaterLst);
        return result;