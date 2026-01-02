from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        length = len(nums);
        halfLen = int(length / 2);
        if length == 0:
            return None;
        elif length == 1:
            obj = TreeNode(nums[0], None, None);
            return obj;
        elif length == 2:
            rightObj = TreeNode(nums[1], None, None);
            obj = TreeNode(nums[0], None, rightObj);
            return obj;
        else:
            centerVal = nums[halfLen];
            leftTree = self.sortedArrayToBST(nums[:halfLen]);
            rightTree = self.sortedArrayToBST(nums[halfLen+1:]);
            return TreeNode(centerVal, leftTree, rightTree);

sol = Solution();
negTen = TreeNode(-10, None, None);
five = TreeNode(5, None, None);
nine = TreeNode(9, five, None);
negThree = TreeNode(-3, negTen, None);
root = TreeNode(0, negThree, nine);
obj = sol.sortedArrayToBST([-10,-3,0,5,9]);
print();