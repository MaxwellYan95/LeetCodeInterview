# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(l1.val+l2.val);
        current = front;
        carry = 0;
        while (l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next
            total = l1.val+l2.val+carry;
            if total >= 10:
                carry = total // 10;
                total = total % 10;
            else:
                carry = 0;
            current.next = ListNode(total, None)
            current = current.next;
        l1 = l1.next
        l2 = l2.next
        current.next = self.leftover(l1, carry);
        current.next = self.leftover(l2, carry);
        return front;

    def leftover(self, l: Optional[ListNode], carry: int):
        if l == None:
            return None
        front = ListNode(l.val+carry);
        current = front;
        while (l.next != None):
            l = l.next
            total = l.val+carry;
            if total >= 10:
                carry = total // 10;
                total = total % 10;
            else:
                carry = 0;
        return front;