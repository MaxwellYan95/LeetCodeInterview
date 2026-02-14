# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        pt1 = head;
        pt2 = head.next;
        while pt2 != None:
            n1 = pt1.val;
            n2 = pt2.val;

            if n1 % 2 == 0 and n2 % 2 == 1:
                pt1.val = n2;
                pt2.val = n1;
            if n1 % 2 == 0 and n2 % 2 == 0:
                pt2 = pt2.next;
            else:
                pt1 = pt1.next;
                pt2 = pt2.next;
        return head;

