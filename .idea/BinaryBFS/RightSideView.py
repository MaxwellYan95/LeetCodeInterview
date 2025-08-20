from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return [];
        elif root.left == None and root.right == None:
            return [root.val];
        result = [root.val];
        rightLst = [];
        leftLst = [];
        if root.left != None:
            leftLst = self.rightSideView(root.left);
        if root.right != None:
            rightLst = self.rightSideView(root.right);
        if len(rightLst) >= len(leftLst):
            result.extend(rightLst);
        else:
            minLen = min(len(rightLst), len(leftLst));
            result.extend(rightLst[:minLen]);
            result.extend(leftLst[minLen:]);
        return result;

sol = Solution();
left3 = TreeNode(5, None, None);
left2 = TreeNode(4, left3, None);
left1 = TreeNode(2, left2, None);
right1 = TreeNode(3, None, None);
root = TreeNode(1, left1, right1);
print(sol.rightSideView(root));
print();