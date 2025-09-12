from collections import defaultdict;

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None;
        value = postorder.pop();
        nextIndex = inorder.index(value);
        rightTree = self.buildTree(inorder[nextIndex+1:], postorder);
        leftTree = self.buildTree(inorder[:nextIndex], postorder);
        return TreeNode(value, leftTree, rightTree);

sol = Solution();
result1 = sol.buildTree([9,3,15,20,7], [9,15,7,20,3]);
result2 = sol.buildTree([2,1], [2,1]);

print();