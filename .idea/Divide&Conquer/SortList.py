from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None;
        if head.next == None:
            return head;
        temp = head;
        fast = head;
        slow = head;
        while fast != None:
            temp = slow;
            slow = slow.next;
            fast = fast.next;
            if fast == None:
                break;
            fast = fast.next;
        temp.next = None;
        left = self.sortList(head);
        right = self.sortList(slow);
        if left == None:
            return right;
        elif right == None:
            return left;
        newHead = ListNode(left.val, None);
        if right.val < left.val:
            newHead = ListNode(right.val, None);
            right = right.next;
        else:
            left = left.next;
        pointer = newHead;
        while left != None and right != None:
            if right.val < left.val:
                pointer.next = ListNode(right.val, None);
                right = right.next;
            else:
                pointer.next = ListNode(left.val, None);
                left = left.next;
            pointer = pointer.next;
        while right != None:
            pointer.next = ListNode(right.val, None);
            right = right.next;
            pointer = pointer.next;
        while left != None:
            pointer.next = ListNode(left.val, None);
            left = left.next;
            pointer = pointer.next;
        return newHead;

sol = Solution()
sol.convertToLinkedList([1, 2, 3, 4]);