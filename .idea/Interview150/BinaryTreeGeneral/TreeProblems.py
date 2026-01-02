from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return 1
        leftHeight = 0
        rightHeight = 0
        if (root.left != None):
            leftHeight = self.maxDepth(root.left)
        if (root.right != None):
            rightHeight = self.maxDepth(root.right)
        if (leftHeight > rightHeight):
            return 1 + leftHeight
        return 1 + rightHeight

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q == None):
            return True
        if (p == None and q != None):
            return False
        if (p != None and q == None):
            return False
        if (p.val != q.val):
            return False
        if (p.left != None and q.left == None):
            return False
        if (p.left == None and q.left != None):
            return False
        if (p.right != None and q.right == None):
            return False
        if (p.right == None and q.right != None):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root.left == None and root.right == None):
            return TreeNode(root.val, root.left, root.right)
        left = None
        right = None
        if (root.left != None):
            left = self.invertTree(root.left)
        if (root.right != None):
            right = self.invertTree(root.right)
        return TreeNode(root.val, right, left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        leftList = self.leftTree(root.left)
        rightList = self.rightTree(root.right)
        if (leftList == rightList):
            return True
        else:
            return False


    def rightTree(self, root: Optional[TreeNode]) -> list[int]:
        list = []
        if root == None:
            return None
        if root.left == None and root.right == None:
            return [root.val]
        if root.left != None:
            leftList = self.leftTree(root.left)
            list.extend(leftList)
        else:
            list.append(None)
        if root.right != None:
            rightList = self.rightTree(root.right)
            list.extend(rightList)
        else:
            list.append(None)
        list.append(root.val)
        return list

    def leftTree(self, root: Optional[TreeNode]) -> list[int]:
        list = []
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        if root.right != None:
            rightList = self.rightTree(root.right)
            list.extend(rightList)
        else:
            list.append(None)
        if root.left != None:
            leftList = self.leftTree(root.left)
            list.extend(leftList)
        else:
            list.append(None)
        list.append(root.val)
        return list

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root.left == None and root.right == None:
            if root.val == targetSum:
                return True
            else:
                return False
        elif root.left == None:
            return self.hasPathSum(root.right, targetSum - root.val)
        elif root.right == None:
            return self.hasPathSum(root.left, targetSum - root.val)
        else:
            return self.hasPathSum(root.right, targetSum - root.val) or self.hasPathSum(root.left, targetSum - root.val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst = self.extractNums(root);
        sum = 0;
        for innerLst in lst:
            place = 0;
            for num in innerLst:
                sum += (num*(10**place));
                place += 1;
        return sum;

    def extractNums(self, root: Optional[TreeNode]) -> (list[list[int]]):
        result = [];
        if root == None:
            return [[0]];
        elif root.left == None and root.right == None:
            return [[root.val]];
        else:
            if root.left != None:
                leftLst = self.extractNums(root.left);
                for lst in leftLst:
                    lstCopy = lst;
                    lstCopy.append(root.val)
                    result.append(lstCopy);
            if root.right != None:
                rightLst = self.extractNums(root.right);
                for lst in rightLst:
                    lstCopy = lst;
                    lstCopy.append(root.val)
                    result.append(lstCopy);
            return result;

    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> TreeNode:
        rightNode = None;
        leftNode = None;
        if (root.right != None):
            rightNode = self.lowestCommonAncestor(root.right, p, q)
        if (root.left != None):
            leftNode = self.lowestCommonAncestor(root.left, p, q)
        if (leftNode != None):
            return leftNode;
        elif (rightNode != None):
            return rightNode;
        else:
            left, right = self.containsPQ(root, p, q)
            if left and right:
                return root;
            else:
                return None

    def containsPQ(self, root: TreeNode, p: TreeNode, q: TreeNode) -> (bool, bool):
        if root == None:
            return (False, False, None)
        conds = [False, False]
        if root.val == p.val:
            conds[0] = True;
        elif root.val == q.val:
            conds[1] = True;
        rightCond = [False, False];
        leftCond = [False, False];
        if root.left != None:
            pCond, qCond = self.ancestorTraversal(root.left, p, q);
            leftCond[0] = pCond;
            leftCond[1] = qCond;
        if root.right != None:
            pCond, qCond = self.ancestorTraversal(root.right, p, q);
            rightCond[0] = pCond;
            rightCond[1] = qCond;
        return (conds[0] or rightCond[0] or leftCond[0], conds[1] or rightCond[1] or leftCond[1]);



sol = Solution()
third1 = TreeNode(5, None, None)
third2 = TreeNode(1, None, None)
second1 = TreeNode(9, third1, third2)
second2 = TreeNode(0, None, None)
root = TreeNode(4, second1, second2)
print()
