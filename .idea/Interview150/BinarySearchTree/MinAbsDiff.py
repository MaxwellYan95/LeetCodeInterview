from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = sorted(self.getList(root))
        diff = 0
        if len(lst) == 0:
            return 0;
        elif len(lst) == 1:
            return lst[0];
        diff = lst[1] - lst[0];
        for index in range(1, len(lst)-1):
            newDiff = lst[index+1] - lst[index];
            if newDiff < diff:
                diff = newDiff;
        return diff;


    def getList(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return [];
        result = [];
        leftLst = [];
        rightLst = [];
        if root.left != None:
            leftLst = self.getList(root.left);
        result.extend(leftLst);
        result.append(root.val);
        if root.right != None:
            rightLst = self.getList(root.right);
        result.extend(rightLst);
        return result;