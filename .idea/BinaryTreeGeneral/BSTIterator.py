from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        lst = self.traverse(root)
        for node in lst:
            self.values.append(node.val)

    def traverse(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if root == None:
            return [];
        lst = [];
        if root.left != None:
            leftLst = self.traverse(root.left)
            lst.extend(leftLst)
        lst.append(root)
        if root.right != None:
            rightLst = self.traverse(root.right)
            lst.extend(rightLst)
        return lst;

    def next(self) -> int:
        num = self.values[0];
        self.values = self.values[1:];
        return num;


    def hasNext(self) -> bool:
        if len(self.values) == 0:
            return False
        return True