# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0);
        current = front;
        carry = 0;
        while (l1 != None or l2 != None or carry != 0):
            val1 = 0;
            if (l1 != None):
                val1 = l1.val;
            val2 = 0;
            if (l2 != None):
                val2 = l2.val;
            total = val1+val2+carry;
            carry = total // 10;
            total = total % 10;
            current.next = ListNode(total, None)
            current = current.next;
            if (l1 != None):
                l1 = l1.next;
            if (l2 != None):
                l2 = l2.next;
        return front.next;