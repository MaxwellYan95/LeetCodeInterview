import collections
from collections import defaultdict;

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def makeDict(self, inorder: list[int]):
        indexDict = defaultdict(int);
        for i in range(len(inorder)):
            indexDict[inorder[i]] = i;
        return indexDict;

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        indexDict = self.makeDict(inorder);
        self.i = 0;
        def recur(start: int, end: int) -> TreeNode:
            if start > end:
                return None;
            value = preorder[self.i]
            self.i += 1;
            index = indexDict[value];
            left = recur(start, index-1);
            right = recur(index+1, end);
            return TreeNode(value, left, right);
        return recur(0, len(preorder)-1)

sol = Solution();
tree = sol.buildTree([3,9,20,15,7], [9,3,15,20,7]);
print();




