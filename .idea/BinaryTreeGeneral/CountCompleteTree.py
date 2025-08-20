from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left = root;
        right = root;
        leftH = 0;
        rightH = 0;
        while left != None:
            left = left.left;
            leftH = leftH + 1;
        while right != None:
            right = right.right;
            rightH = rightH + 1;
        if rightH == leftH:
            return 2**(rightH) - 1;
        return 1 + self.countNodes(root.left) + self.countNodes(root.right);


sol = Solution();
four = TreeNode(4, None, None);
two = TreeNode(2, four, None);
three = TreeNode(3, None, None);
one = TreeNode(1, two, three);
print(sol.countNodes(one));