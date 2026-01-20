# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        width = 1;
        maxWidth = 1;
        stack = [];
        if root.left != None:
            stack.append(root.left)
        if root.right != None:
            stack.append(root.right);
        if len(stack) == 2:
            width = 2;
        while len(stack) == 2:
            maxWidth = max(maxWidth, width)
            rightTree = stack.pop();
            leftTree = stack.pop();
            width *= 2;
            if leftTree.left != None:
                stack.append(leftTree.left);
            elif leftTree.right != None:
                width -= 1;
                stack.append(leftTree.right);
            else:
                return maxWidth;
            if rightTree.right != None:
                stack.append(rightTree.right);
            elif rightTree.left != None:
                width -= 1;
                stack.append(rightTree.left);
            else:
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


