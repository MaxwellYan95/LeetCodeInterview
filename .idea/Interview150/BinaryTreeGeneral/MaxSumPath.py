# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxVal = 0;

    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0;
        self.maxVal = root.val
        def maxPath(root: TreeNode):
            if root == None:
                return 0;
            rightMax = maxPath(root.right)
            leftMax = maxPath(root.left);
            self.maxVal = max(self.maxVal, root.val+rightMax+leftMax)
            self.maxVal = max(self.maxVal, root.val+max(rightMax, leftMax))
            self.maxVal = max(self.maxVal, root.val)
            return max(root.val, root.val + max(rightMax, leftMax));
        maxPath(root)
        return self.maxVal;

sol = Solution()
nine = TreeNode(9)
b1 = TreeNode(15)
b2 = TreeNode(7)
b = TreeNode(20, b1, b2)
r = TreeNode(-10, nine, b)
print(sol.maxPathSum(r))



