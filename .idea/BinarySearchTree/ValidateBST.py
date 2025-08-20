from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = self.extractLst(root);
        sortedLst = sorted(lst);
        for index in range(len(lst)-1):
            if lst[index] != sortedLst[index]:
                return False;
            if lst[index] == lst[index+1]:
                return False;
        if lst[len(lst)-1] != sortedLst[len(lst)-1]:
            return False;
        return True;

    def extractLst(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return [];
        result = [];
        leftLst = [];
        rightLst = [];
        if root.left != None:
            leftLst = self.extractLst(root.left);
        result.extend(leftLst);
        result.append(root.val);
        if root.right != None:
            rightLst = self.extractLst(root.right);
        result.extend(rightLst);
        return result;