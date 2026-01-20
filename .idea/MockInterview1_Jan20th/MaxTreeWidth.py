from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        collect = deque([(root, 1)])
        maxWidth = 0;
        while len(collect) != 0:
            n = len(collect);
            _, start = collect[0]
            for _ in range(n):
                tree, index = collect.popleft();
                if tree.left != None:
                    collect.append((tree.left, index*2))
                if tree.right != None:
                    collect.append((tree.right, index*2+1));
                maxWidth = max(maxWidth, index-start+1);
        return maxWidth;


sol = Solution()
six = TreeNode(6)
five = TreeNode(5, six, None)
three = TreeNode(3, five, None)
seven = TreeNode(7)
nine = TreeNode(9, seven, None)
two = TreeNode(2, None, nine)
one = TreeNode(1, three, two)
result = sol.widthOfBinaryTree(one)
print(result)


