

# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.results = 0;

        # stores max of each node
        self.stack = [-(10**4)-1];
        def dfs(root: TreeNode):
            if root == None:
                return;
            last = self.stack[len(self.stack)-1]
            if root.val >= last:
                self.results += 1;
            self.stack.append(max(root.val, last));
            dfs(root.left)
            dfs(root.right)
            self.stack.pop(len(self.stack)-1);
        dfs(root)
        return self.results

sol = Solution()
left2 = TreeNode(3);
left1 = TreeNode(1, left2);
rightRight = TreeNode(5);
rightLeft = TreeNode(1);
right = TreeNode(4, rightLeft, rightRight);
root = TreeNode(3, left1, right);

print(sol.goodNodes(root))
