# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head;
        while head != None and head.val == val:
            head = head.next;
        traverse = head;
        while traverse != None:
            if traverse.next != None:
                if traverse.next.val == val:
                    traverse.next = traverse.next.next;
                else:
                    traverse = traverse.next
            else:
                traverse = traverse.next
        return head;