# Definition for a binary tree node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
