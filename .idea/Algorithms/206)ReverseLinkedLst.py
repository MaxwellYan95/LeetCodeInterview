# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None;
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next;
        lst.reverse();
        front = ListNode(lst[0])
        current = front;
        for num in lst[1:]:
            current.next = ListNode(num)
            current = current.next;
        return front
