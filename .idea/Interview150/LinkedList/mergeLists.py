from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2;
        if list2 == None:
            return list1;
        node1 = list1
        node2 = list2
        front = None;
        if node1.val < node2.val:
            front = ListNode(node1.val, None)
            node1 = node1.next;
        else:
            front = ListNode(node2.val, None)
            node2 = node2.next
        back = front;
        while node1 != None and node2 != None:
            if node1.val < node2.val:
                back.next = ListNode(node1.val, None)
                node1 = node1.next;
            else:
                back.next = ListNode(node2.val, None)
                node2 = node2.next
            back = back.next;
        while node1 != None:
            back.next = ListNode(node1.val, None)
            node1 = node1.next;
            back = back.next;
        while node2 != None:
            back.next = ListNode(node2.val, None)
            node2 = node2.next
            back = back.next
        return front
