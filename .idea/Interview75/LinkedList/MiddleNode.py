# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if head.next == None:
            return None
        lastInd = 0;
        current = head;
        while current != None:
            current = current.next
            lastInd += 1;
        middle = lastInd // 2;
        counter = 0;
        current = head;
        newFront = current;
        for i in range(middle-1):
            current = current.next;
        current.next = current.next.next;
        return newFront

sol = Solution()
five = ListNode(5)
four = ListNode(4, five);
three = ListNode(3, four);
two = ListNode(2, three);
one = ListNode(1, two);
print(sol.deleteMiddle(one))