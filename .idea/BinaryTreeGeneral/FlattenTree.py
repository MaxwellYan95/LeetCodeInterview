from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None;
        if root.left == None and root.right == None:
            return root;
        leftTree = self.flatten(root.left);
        rightTree = self.flatten(root.right);
        if leftTree == None:
            root.left = None;
            root.right = rightTree;
            return root;
        if rightTree == None:
            root.left = None;
            root.right = leftTree;
            return root;
        traversal = leftTree;
        while traversal.right != None:
            traversal = traversal.right;
        traversal.right = rightTree;
        root.left = None;
        root.right = leftTree;
        return root;
