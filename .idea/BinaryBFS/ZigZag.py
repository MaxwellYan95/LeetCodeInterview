from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        return self.traverse(root, 1);

    def traverse(self, root: Optional[TreeNode], leftCounter: int) -> list[list[int]]:
        if root == None:
            return [];
        if root.left == None and root.right == None:
            return [[root.val]];
        left = [];
        right = [];
        if leftCounter == 1:
            left = self.traverse(root.left, 0);
            right = self.traverse(root.right, 0);
        else:
            left = self.traverse(root.left, 1);
            right = self.traverse(root.right, 1);
        result = [[root.val]];
        if len(left) > len(right):
            for i in range(len(left) - len(right)):
                right.append([]);
        else:
            for i in range(len(right) - len(left)):
                left.append([]);
        curLeft = leftCounter;
        if curLeft == 1:
            curLeft = 0;
        else:
            curLeft = 1;
        for index in range(len(right)):
            if curLeft == 1:
                lst = left[index];
                lst.extend(right[index]);
                curLeft = 0;
            else:
                lst = right[index];
                lst.extend(left[index]);
                curLeft = 1;
            result.append(lst);
        return result;

sol = Solution();
rightLeft = TreeNode(15, None, None);
rightRight = TreeNode(7, None, None);
right = TreeNode(20, rightLeft, rightRight);
left = TreeNode(9, None, None);
root = TreeNode(3, left, right);
print(sol.zigzagLevelOrder(root));
print();