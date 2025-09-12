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
        for index in range(len(inorder)):
            indexDict[inorder[index]] = index;
        return indexDict;

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        self.index = len(postorder)-1;
        indexDict = self.makeDict(inorder);
        def recur(inorder: list[int], counter: int):
            if self.index == 0:
                return TreeNode(postorder[0]);
            value = postorder[self.index];
            nextIndex = indexDict[value] - counter;
            if len(inorder) == 1:
                return TreeNode(value);
            rightTree = None;
            leftTree = None;
            self.index = self.index-1;
            if self.index >= 0:
                rightTree = recur(inorder[nextIndex+1:], nextIndex+1);
            self.index = self.index-1;
            if self.index >= 0:
                leftTree = recur(inorder[:nextIndex], -nextIndex+1);
            return TreeNode(value, leftTree, rightTree);
        return recur(inorder, 0);

sol = Solution();
result1 = sol.buildTree([9,3,15,20,7], [9,15,7,20,3]);
result2 = sol.buildTree([2,1], [2,1]);

print();