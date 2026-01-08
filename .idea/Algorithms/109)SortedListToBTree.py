# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        tree = TreeNode(head.val);
        current = head;
        current = current.next;
        while current != None:
            self.insertIntoBST(tree, current.val);
        return tree;


    def insertIntoBST(self, tree: TreeNode, value: int):
        front = tree;
        if (value < front.val):
            if (front.left == None):
                front.left = TreeNode(value)
            else:
                self.insertIntoBST(front.left, value)
        else:
            if (front.right == None):
                front.right = TreeNode(value)
            else:
                self.insertIntoBST(front.right, value)