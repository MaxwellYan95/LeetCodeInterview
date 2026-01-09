class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0;
        if root.left == None and root.right == None:
            return 1;
        left = math.inf;
        right = math.inf;
        if root.left != None:
            left = self.minDepth(root.left);
        if root.right != None:
            right = self.minDepth(root.right);
        return 1 + min(left, right);
