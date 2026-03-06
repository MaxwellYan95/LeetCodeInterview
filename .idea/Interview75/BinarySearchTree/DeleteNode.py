# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root;
        treeLst = self.treeToList(root);
        if key not in treeLst:
            return root;
        treeLst.remove(key);
        return self.lstToTree(treeLst)


    def treeToList(self, root: TreeNode) -> list[int]:
        stack = [root]
        lst = []
        while stack:
            node = stack.pop();
            lst.append(node.val)
            if node.left != None:
                stack.append(node.left);
            if node.right != None:
                stack.append(node.right);
        return lst;

    def lstToTree(self, root: list[int]) -> TreeNode:
        if len(root) == 0:
            return None;
        front = TreeNode(root[0]);
        for num in root[1:]:
            self.insertToTree(front, num)
        return front;

    def insertToTree(self, root: TreeNode, val: int):
        if val > root.val and root.right == None:
            root.right = TreeNode(val)
        elif val < root.val and root.left == None:
            root.left = TreeNode(val)
        elif val > root.val:
            self.insertToTree(root.right, val)
        elif val < root.val:
            self.insertToTree(root.left, val)

tree1 = TreeNode(0)
