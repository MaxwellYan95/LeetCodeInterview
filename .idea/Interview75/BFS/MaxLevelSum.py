# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 0;
        maxLvl = 0;
        maxTotal = -float('inf');
        stack = [root];
        while stack:
            total = 0;
            n = len(stack);
            for i in range(n):
                node = stack.pop(0);
                total += node.val;
                if node.left != None:
                    stack.append(node.left)
                if node.right != None:
                    stack.append(node.right)
            level += 1;
            if maxTotal < total:
                maxTotal = total;
                maxLvl = level;
        return maxLvl



