# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return ["" + str(root.val)]
        lst = [];
        leftLst = self.binaryTreePaths(root.left);
        rightLst = self.binaryTreePaths(root.right);
        for string in leftLst + rightLst:
            lst.append(str(root.val) + "->" + string);
        return lst;