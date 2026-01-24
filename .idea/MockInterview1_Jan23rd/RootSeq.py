# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1 = self.findLeafSeq(root1);
        seq2 = self.findLeafSeq(root2);
        return seq1 == seq2;

    def findLeafSeq(self, root: TreeNode):
        if root.left == None and root.right == None:
            return [root.val]
        leftLst = []
        rightLst = []
        if root.left != None:
            leftLst = self.findLeafSeq(root.left)
        if root.right != None:
            rightLst = self.findLeafSeq(root.right)
        return leftLst + rightLst;
