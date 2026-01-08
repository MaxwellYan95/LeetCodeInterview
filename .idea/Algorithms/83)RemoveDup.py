# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None;
        front = ListNode(head.val)
        current = front;
        ptr = head;
        ptr = ptr.next;

        while ptr != None:
            if ptr.val != current.val:
                current.next = ListNode(ptr.val)
                current = current.next;
            ptr = ptr.next;
        return front;
