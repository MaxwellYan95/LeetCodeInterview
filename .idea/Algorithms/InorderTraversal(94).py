# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return [];
        if root.left == None and root.right == None:
            return [root.val];
        leftLst = [];
        if root.left != None:
            leftLst = self.inorderTraversal(root.left)
        rightLst = [];
        if root.right != None:
            rightLst = self.inorderTraversal(root.right)
        result = [];
        result.extend(leftLst);
        result.append(root.val);
        result.extend(rightLst);
        return result;