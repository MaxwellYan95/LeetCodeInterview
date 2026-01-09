from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    mapping = defaultdict(int)

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        elif root.left == None and root.right == None:
            self.mapping[root] = 1;
            return True
        left = None
        leftSize = 0
        right = None
        rightSize = 0
        if root.left != None:
            left = self.isBalanced(root.left)
            leftSize = self.mapping[root.left];
        if root.right != None:
            right = self.isBalanced(root.right)
            rightSize = self.mapping[root.right];
        self.mapping[root] = max(rightSize, leftSize) + 1
        if abs(leftSize - rightSize) > 1:
            return False;
        if left == False or right == False:
            return False
        return True;

sol = Solution()
three1 = TreeNode(3)
three2 = TreeNode(3)
two1 = TreeNode(2, three1, None);
two2 = TreeNode(2, None, three2);
one = TreeNode(1, two1, two2);
temp = sol.isBalanced(one);
print();