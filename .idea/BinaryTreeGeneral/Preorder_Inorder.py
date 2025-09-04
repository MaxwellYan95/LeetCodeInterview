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

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        indexDict = self.makeDict(inorder);
        def recur(preorder: list[int], inorder: list[int]) -> TreeNode:
            if (len(preorder) == 0):
                return None;
            if (len(inorder) == 0):
                return TreeNode(preorder[0]);
            root = TreeNode(preorder[0]);
            index = indexDict[preorder[0]];
            leftTree = self.buildTree(preorder[1:], inorder[index+1:]);
            rightTree = self.buildTree(preorder[2:], inorder[:index]);
            root.left = leftTree;
            root.right = rightTree;
            return root;
        return recur(preorder, inorder);
sol = Solution();
tree = sol.buildTree([3,9,20,15,7], [9,3,15,20,7]);
print();




