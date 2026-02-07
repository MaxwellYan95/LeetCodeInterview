# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Using BFS
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return []
        stack = [root];
        result = []
        while stack:
            maxVal = -float('inf')
            nodes = stack.copy()
            stack = []
            for n in nodes:
                maxVal = max(maxVal, n.val)
            for n in nodes:
                if n.left != None:
                    stack.append(n.left)
                if n.right != None:
                    stack.append(n.right)
            result.append(maxVal)
        return result
