from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lenOfList(head);
        return self.removeNthFromEndLen(head, n, length);

    def removeNthFromEndLen(self, head: Optional[ListNode], n: int, length: int) -> Optional[ListNode]:
        if length == 0:
            return None;
        curHead = self.removeNthFromEndLen(head.next, n, length-1);
        if n == length:
            return curHead;
        else:
            return ListNode(head.val, curHead);

    def lenOfList(self, head: Optional[ListNode]) -> int:
        if head == None:
            return 0;
        if head.next == None:
            return 1;
        return self.lenOfList(head.next) + 1;

sol = Solution();
five = ListNode(5, None);
four = ListNode(4, five);
three = ListNode(3, four);
two = ListNode(2, three);
one = ListNode(1, two);
sol.removeNthFromEnd(one, 2);