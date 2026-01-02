from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root == None:
            return [];
        result = [[root.val]];
        leftLst = [];
        rightLst = [];
        if (root.left != None):
            leftLst = self.levelOrder(root.left);
        if (root.right != None):
            rightLst = self.levelOrder(root.right);
        minLen = min(len(leftLst), len(rightLst));
        longerLst = [];
        if len(leftLst) > len(rightLst):
            longerLst = leftLst[minLen:];
        else:
            longerLst = rightLst[minLen:];
        for index in range(minLen):
            lst = leftLst[index] + rightLst[index];
            result.append(lst);
        result.extend(longerLst);
        return result;

sol = Solution();
left3 = TreeNode(5, None, None);
left2 = TreeNode(4, left3, None);
left1 = TreeNode(2, left2, None);
right1 = TreeNode(3, None, None);
root = TreeNode(1, left1, right1);
print(sol.levelOrder(root));