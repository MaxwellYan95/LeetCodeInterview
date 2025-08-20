from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = self.extractLst(root);
        return lst[k-1];
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