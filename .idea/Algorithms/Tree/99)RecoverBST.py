# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def findMistake(start: TreeNode, node: TreeNode, isLeft: bool):
            if node == None:
                return;
            if isLeft and start.val < node.val:
                temp = node.val;
                node.val = start.val;
                start.val = temp;
            if not isLeft and start.val > node.val:
                temp = node.val;
                node.val = start.val;
                start.val = temp;
            findMistake(start, node.left, isLeft)
            findMistake(start, node.right, isLeft);
        """
        Use BFS inside
        """
        stack = [];
        stack.append(root);
        while stack:
            current = stack.pop();
            left = False;
            right = False;
            prevVal = current.val
            if current.left != None:
                stack.append(current.left)
                findMistake(current, current.left, True)
            if current.right != None:
                stack.append(current.right)
                findMistake(current, current.right, False)
            if prevVal != current.val:
                stack.append(current)

sol = Solution();
three = TreeNode(3)
one = TreeNode(1);
root = TreeNode(2, three, one);
sol.recoverTree(root)

