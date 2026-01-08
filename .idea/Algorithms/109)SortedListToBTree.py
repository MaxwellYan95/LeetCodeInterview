
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
        if head == None:
            return None;
        lst = self.listToArray(head)
        return self.listToTree(lst)

    def listToArray(self, head: ListNode) -> list[int]:
        lst = [head.val]
        current = head;
        current = current.next;
        while current != None:
            lst.append(current.val);
            current = current.next;
        return lst

    def listToTree(self, lst: list[int]) -> TreeNode:
        if len(lst) == 0:
            return None;
        if len(lst) == 1:
            return TreeNode(lst[0])
        midInd = (len(lst)) // 2;
        leftTree = listToTree(lst[:midInd])
        rightTree = listToTree(lst[midInd+1:])
        tree = TreeNode(lst[midInd]);
        tree.left = leftTree;
        tree.right = rightTree;
        return tree

sol = Solution();
last = ListNode(3)
middle = ListNode(2, last)
front = ListNode(1, middle)
tree = sol.sortedListToBST(front)
print();